import tkinter as tk
from tkinter import messagebox, ttk
import random
from Components.Map.Grid import Grid
from Components.Searchers.Searcher import Searcher
from time import *


class UIVisualize(tk.Tk):
    def __init__(self, rows: int, cols: int, typeOfSearch: str, customCellSize: int = None) -> None:
        super().__init__()
        self.title("Pathfinding visualizer by Simon")
        self.configure(bg='#cedbec')
        self.rows, self.cols = rows, cols
        if customCellSize is None:
            if self.rows <= 30 or self.cols <= 25:
                self.cell_size = 25
            else:
                self.cell_size = 22
        else:
            self.cell_size = customCellSize

        self.geometry('+600+100')
        self.startColor = (255, 221, 0)
        self.endColor = (235, 10, 30)
        self.startPoint, self.endPoint = None, None
        self.walls = []
        self.g = Grid(self.cols, self.rows)
        self.buttonFont = ('Arial', 12)
        self.isChoosingStart, self.isChoosingGoal, self.isChoosingWall = False, False, False
        self.canvas = tk.Canvas(self, width=self.rows * self.cell_size,
                                height=self.cols * self.cell_size, bg='white')
        self.canvas.pack()
        self.type = typeOfSearch

    def _drawChanges(self, result: list = None, changes: list = None):
        if changes is not None:
            for cell, dType in changes:
                if (cell == self.startPoint or cell == self.endPoint):
                    continue
                x1, y1 = cell[0] * self.cell_size, cell[1] * self.cell_size
                x2, y2 = (cell[0] + 1) * \
                    self.cell_size, (cell[1] + 1) * self.cell_size
                color = '#fbaab1'if dType == 'frontier' else '#fdd0d4'
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
                sleep(0.0001)
                self.update()

        for cell in result:
            x, y = (cell.x, cell.y)
            self.canvas.create_rectangle(x * self.cell_size, y * self.cell_size, x *
                                         self.cell_size + self.cell_size, y * self.cell_size + self.cell_size, fill='green')
            self.update()

    def _drawGrid(self):
        self.canvas.delete("all")
        for i in range(self.cols):
            for j in range(self.rows):
                x1, y1 = i * self.cell_size, j * self.cell_size
                x2, y2 = (i+1) * self.cell_size, (j+1) * self.cell_size

                self.cell_type = self.grid[i][j]
                color = '#cedbec'
                if self.cell_type == 'start':
                    color = '#ffdd00'
                elif self.cell_type == 'end':
                    color = '#eb0a1e'
                elif self.cell_type == 'wall':
                    color = '#000000'

                self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color, outline='#0c4da2')

    def _setStart(self, row: int, col: int):
        if self.startPoint:
            self.grid[self.startPoint[0]][self.startPoint[1]] = 'e'
        self.startPoint = (row, col)
        print(self.startPoint)
        self.grid[row][col] = 'start'
        self._drawGrid()

    def _setGoal(self, row: int, col: int):
        if self.endPoint and (self.endPoint[0] >= 0 and self.endPoint[0] <= self.cols) and (self.endPoint[1] >= 0 and self.endPoint[1] <= self.rows):
            self.grid[self.endPoint[0]][self.endPoint[1]] = 'e'
        self.endPoint = (row, col)
        print(self.endPoint)
        if self.grid and (row >= 0 and row < self.cols) and (col >= 0 and col < self.rows):
            self.grid[row][col] = 'end'

        self._drawGrid()

    def _setWall(self, row: int, col: int):
        if self.grid[row][col] == 'start' or self.grid[row][col] == 'end':
            return
        self.grid[row][col] = 'wall'
        self.walls.append((row, col, 1, 1))
        self._drawGrid()

    def _randWall(self):
        self._clearMap()
        self.startPoint = None
        self.endPoint = None
        for i in range(self.cols):
            for j in range(self.rows):
                if random.random() < 0.2:
                    self.grid[i][j] = 'wall'
                    self._setWall(i, j)
                else:
                    self.grid[i][j] = 'e'
        print(self.grid)
        print(self.g.grid)
        self._drawGrid()

    def _clearMap(self):
        self.startPoint = None
        self.endPoint = None
        self.walls = []
        for i in range(self.cols):
            for j in range(self.rows):
                self.grid[i][j] = 'e'
        self.g.grid = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        self._drawGrid()

    def _setState(self, state: str):
        self.isChoosingStart = state == 'start'
        self.isChoosingGoal = state == 'goal'
        self.isChoosingWall = state == 'wall'

    def _handleMouseClick(self, e: tk.Event):
        col = e.y // self.cell_size
        row = e.x // self.cell_size

        if (row >= 0 and row < self.cols) and (col >= 0 and col < self.rows):
            if self.isChoosingStart:
                if self.grid[row][col] == 'wall':
                    return
                self._setStart(row, col)
            elif self.isChoosingGoal:
                if self.grid[row][col] == 'wall':
                    return
                self._setGoal(row, col)
            elif self.isChoosingWall:
                self._setWall(row, col)

            if not self.isChoosingWall:
                self._drawGrid()

    def _visualizePath(self):
        if self.startPoint and self.endPoint:
            start = self.startPoint
            goal = self.endPoint
            searcher = Searcher(self.g, start, goal, self.type)
            for wall in self.walls:
                self.g.appendWall(*wall)
            start = time()
            result, cNodes, changes = searcher.getResult()
            print(f"Time taken for {self.type}: ", (time() - start) * 1000.0)
            print(f"Nodes for {self.type}: {cNodes}")
            if result:
                self._drawChanges(result, changes)

            else:
                messagebox.showinfo(
                    "No path found", "No path found in this scenario!")

    def _convertName(self, name: str) -> str:
        match name:
            case 'bfs':
                return 'Breadth First Search'
            case 'dfs':
                return 'Depth First Search'
            case 'cus1':
                return 'Iterative Deepening DLS'
            case 'gbfs':
                return 'Greedy Best-First Search'
            case 'as':
                return 'A*'
            case 'cus2':
                return 'Weighted A*'

    def mainloop(self, n: int = 0) -> None:
        self.grid = [['e' for _ in range(self.rows)] for _ in range(self.cols)]

        self._drawGrid()

        self.canvas.bind('<ButtonRelease-1>', self._handleMouseClick)
        self.canvas.bind('<B1-Motion>', self._handleMouseClick)

        self.buttonFont = ('Arial', 12)
        self.startButton = tk.Button(self, text="Start Point", font=self.buttonFont, bg='#9eb8da', activebackground='#3d71b5',
                                     activeforeground='#eb0a1e', fg='#0c4da2', command=lambda: self._setState('start'))
        self.startButton.pack(side=tk.LEFT, padx=5)

        self.endButton = tk.Button(self, text="Goal Point", font=self.buttonFont, bg='#9eb8da', activebackground='#3d71b5',
                                   activeforeground='#eb0a1e', fg='#0c4da2', command=lambda: self._setState('goal'))
        self.endButton.pack(side=tk.LEFT, padx=10)

        self.wallButton = tk.Button(self, text="Set Walls", font=self.buttonFont, bg='#9eb8da', activebackground='#3d71b5',
                                    activeforeground='#eb0a1e', fg='#0c4da2', command=lambda: self._setState('wall'))
        self.wallButton.pack(side=tk.LEFT, padx=15)

        self.randomWall = tk.Button(self, text="Random Walls", font=self.buttonFont, bg='#9eb8da', activebackground='#3d71b5',
                                    activeforeground='#eb0a1e', fg='#0c4da2', command=lambda: self._randWall())
        self.randomWall.pack(side=tk.LEFT, padx=15)

        self.clearButton = tk.Button(self, text="Clear All", font=self.buttonFont, bg='#9eb8da', activebackground='#3d71b5', activeforeground='#eb0a1e',
                                     fg='#0c4da2', command=lambda: self._clearMap())  # Added parentheses after clearMap
        self.clearButton.pack(side=tk.LEFT, padx=15)

        self.visualizeButton = tk.Button(self, text="Visualize Path", font=self.buttonFont, bg='#9eb8da', activebackground='#3d71b5',
                                         activeforeground='#eb0a1e', fg='#0c4da2', command=lambda: self._visualizePath())
        self.visualizeButton.pack(side=tk.LEFT, padx=15)

        tk.Label(self, font=('Arial', 18), text=f"{self._convertName(self.type)}", bg='#cedbec', fg='black', height=2, width=len(self._convertName(self.type))).pack(
            side=tk.LEFT, padx=15)

        return super().mainloop(n)


class MainUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Pathfinding Visualizer by Simon")
        self.geometry('+600+300')
        self.configure(bg='white')
        self.buttonFont = ('Arial', 15)
        self._drawOutline()

    def _drawOutline(self):
        tk.Label(self, text="Rows: ", font=self.buttonFont,
                 bg='white', foreground='black').grid(row=0, column=0, padx=10, pady=10)
        self.rows_entry = tk.Entry(self, font=self.buttonFont)
        self.rows_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self, text="Columns: ", font=self.buttonFont,
                 bg='white', foreground='black').grid(row=1, column=0, padx=10, pady=10)
        self.cols_entry = tk.Entry(self, font=self.buttonFont)
        self.cols_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self, text="Cell Size: ", font=self.buttonFont, bg='white', foreground='black').grid(
            row=2, column=0, padx=10, pady=10)
        self.cell_size_entry = tk.Entry(self, font=self.buttonFont)
        self.cell_size_entry.insert(0, '25')
        self.cell_size_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self, text="Type of Search: ", font=self.buttonFont,
                 bg='white', foreground='black').grid(row=3, column=0, padx=10, pady=10)
        self.searchType = ttk.Combobox(self, values=[
            'BFS', 'DFS', 'Iterative Deepning DLS', 'Greedy Best-First Search', 'A*', 'Weighted A*'], font=self.buttonFont)
        self.searchType.grid(row=3, column=1, padx=10, pady=10)

        self.startButton = tk.Button(self, text="Start", font=self.buttonFont, bg='#9eb8da', activebackground='#3d71b5',
                                     activeforeground='#eb0a1e', fg='#0c4da2', command=lambda: self._onPress())
        self.startButton.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        tk.Label(self, font=self.buttonFont, text="Pathfinding Visualizer", bg='white', foreground='black', height=1,
                 width=50).grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        tk.Label(self, font=self.buttonFont, text="Created By: Xuan Tuan Minh Nguyen", bg='white', foreground='black', height=1,
                 width=50).grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        tk.Label(self, font=self.buttonFont, text="Student ID: 103819212", bg='white', foreground='black', height=2,
                 width=40).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def _convertToInt(self, value: str) -> int:
        if value:
            try:
                return int(value)
            except ValueError:
                messagebox.showerror(
                    "Error", f"Please ensure that the the value of {value} must be integer")
                return 0
        else:
            messagebox.showerror(
                "Error", "Please ensure that the fields of rows, columns and cell size are not empty")
            return 0

    def _onPress(self):
        rows, cols, cellSize = self._convertToInt(self.rows_entry.get(
        )), self._convertToInt(self.cols_entry.get()), self._convertToInt(self.cell_size_entry.get())
        searchInput = self.searchType.get()
        searchType = None
        match searchInput:
            case 'BFS':
                searchType = 'bfs'
            case 'DFS':
                searchType = 'dfs'
            case 'Iterative Deepning DLS':
                searchType = 'cus1'
            case 'Greedy Best-First Search':
                searchType = 'gbfs'
            case 'A*':
                searchType = 'as'
            case 'Weighted A*':
                searchType = 'cus2'
            case _:
                messagebox.showerror(
                    "Error", "Please ensure that the search type is selected")

        if rows < 2 and cols < 2:
            messagebox.showerror(
                "Error", "Make sure that the range of rows and cols must be from the range of[2, 30]")
        elif rows > 30 and cols > 30:
            messagebox.showerror(
                "Error", "Make sure that the range of rows and cols must be from the range of[2, 30]")

        else:
            UIVisualize(rows, cols, searchType, cellSize).mainloop()
