import tkinter as tk
import heapq
import math
import random
from time import sleep
root = tk.Tk()
root.title("A* Pathfinding Visualizer")

root.configure(bg='#cedbec')

width, height = 30, 25
cell_size = 30
root.geometry('+520+100')

start_color = (255, 221, 0)
end_color = (235, 10, 30)

start = None
goal = None

is_setting_start = False
is_setting_goal = False
is_setting_wall = False


def heuristic(cell, goal):
    if goal is not None:
        return math.sqrt((cell[0] - goal[0])**2 + (cell[1] - goal[1])**2)
    else:
        return 0


def a_star(grid, start, goal):
    open_set = [(0, start)]
    closed_set = set()
    paths = {start: (None, 0)}
    changes = []

    while open_set:
        _, current_cell = heapq.heappop(open_set)

        if current_cell == goal:
            path = []

            while current_cell:
                path.append(current_cell)
                current_cell, _ = paths[current_cell]
            return path[::-1], changes

        if current_cell in closed_set:
            continue

        closed_set.add(current_cell)

        changes.append((current_cell, 'closed_set'))

        for neighbor in get_neighbors(grid, current_cell):
            tentative_g = paths[current_cell][1] + 1

            if neighbor not in paths or tentative_g < paths[neighbor][1]:
                paths[neighbor] = (current_cell, tentative_g)
                f_value = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_value, neighbor))

                changes.append((neighbor, 'open_set'))

    return [], []


def get_neighbors(grid, cell):
    row, col = cell
    neighbors = [(row + 1, col),
                 (row - 1, col),
                 (row, col + 1),
                 (row, col - 1)]

    return [(r, c) for r, c in neighbors if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] != 'wall']


def draw_changes(changes):

    for cell, cell_type in changes:
        x1, y1 = cell[1] * cell_size, cell[0] * cell_size
        x2, y2 = (cell[1] + 1) * cell_size, (cell[0] + 1) * cell_size
        if cell_type == 'open_set':
            color = '#fbaab1'
        elif cell_type == 'closed_set':
            color = '#fdd0d4'

        # , activefill='#006b4e', activeoutline='#006b4e'
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='#fbaab1')


def draw_grid():
    canvas.delete("all")
    for i in range(width):
        for j in range(height):
            x1, y1 = i * cell_size, j * cell_size
            x2, y2 = (i + 1) * cell_size, (j + 1) * cell_size

            cell_type = grid[j][i]

            color = '#cedbec'
            if cell_type == 'start':
                color = '#FFDD00'
            elif cell_type == 'goal':
                color = '#eb0a1e'
            elif cell_type == 'wall':
                color = '#0c4da2'

            canvas.create_rectangle(
                x1, y1, x2, y2, fill=color, outline='#0c4da2')

    path, changes = a_star(grid, start, goal)
    print("Path: ", path)
    print("Changes: ", changes)
    draw_changes(changes)  # Draw changes after A* is complete

    num_steps = len(path)

    for step, cell in enumerate(path):
        x1, y1 = cell[1] * cell_size + \
            cell_size // 16, cell[0] * cell_size + cell_size // 16
        x2, y2 = (cell[1] + 1) * cell_size - \
            cell_size // 16, (cell[0] + 1) * cell_size - cell_size // 16

        gradient_factor = step / (num_steps - 1)
        current_color = calculate_gradient_color(start_color,
                                                 end_color,
                                                 gradient_factor)
        print(current_color)
        hex_color = "#{:02X}{:02X}{:02X}".format(*current_color)

        # , activefill='#006b4e', activeoutline='#006b4e'
        canvas.create_rectangle(
            x1, y1, x2, y2, fill=hex_color, outline=hex_color)


def calculate_gradient_color(start_color, end_color, factor):
    return tuple(int(start + (end - start) * factor)
                 for start, end in zip(start_color, end_color))


def handle_mouse_click(event):
    global is_setting_start, is_setting_goal, is_setting_wall

    col = event.x // cell_size
    row = event.y // cell_size

    if 0 <= row < height and 0 <= col < width:
        if is_setting_start:
            if grid[row][col] == 'wall':
                return
            set_start(row, col)
        elif is_setting_goal:
            if grid[row][col] == 'wall':
                return
            set_goal(row, col)
            draw_grid()
        elif is_setting_wall:
            toggle_wall(row, col)

        if not is_setting_wall:
            draw_grid()


def set_start(row, col):
    global start
    if start:
        grid[start[0]][start[1]] = 'empty'
    start = (row, col)
    grid[row][col] = 'start'
    draw_grid()


def set_goal(row, col):
    global goal
    if goal and 0 <= goal[0] < height and 0 <= goal[1] < width:
        grid[goal[0]][goal[1]] = 'empty'
    goal = (row, col)
    if grid and 0 <= row < height and 0 <= col < width:
        grid[row][col] = 'goal'
    draw_grid()


def toggle_wall(row, col):
    if grid[row][col] == 'wall':
        grid[row][col] = 'empty'
    else:
        grid[row][col] = 'wall'
    draw_grid()


def restart():
    global start, goal
    start = None
    goal = None
    for i in range(height):
        for j in range(width):
            grid[i][j] = 'empty'
    draw_grid()


def set_mode(mode):
    global is_setting_start, is_setting_goal, is_setting_wall
    is_setting_start = mode == 'start'
    is_setting_goal = mode == 'goal'
    is_setting_wall = mode == 'wall'


def generate_random_maze():
    global start, goal
    start = None
    goal = None
    for i in range(height):
        for j in range(width):
            if random.random() < 0.2:
                grid[i][j] = 'wall'
            else:
                grid[i][j] = 'empty'

    draw_grid()


# write a description for all of this functions
grid = [['empty' for _ in range(width)] for _ in range(height)]
canvas = tk.Canvas(root, width=width * cell_size,
                   height=height * cell_size, bg='white')
canvas.pack()

draw_grid()

canvas.bind('<ButtonRelease-1>', handle_mouse_click)
canvas.bind('<B1-Motion>', handle_mouse_click)

button_font = ('Helvetica', 12, "bold")
start_button = tk.Button(root, text="Set Start",
                         font=button_font, bg='#9eb8da',
                         fg='#0c4da2', activebackground='#3d71b5',
                         activeforeground='#eb0a1e',
                         command=lambda: set_mode('start'))
start_button.pack(side=tk.LEFT, padx=5)
goal_button = tk.Button(root, text="Set Goal",
                        font=button_font, bg='#9eb8da',
                        fg='#0c4da2', activebackground='#3d71b5',
                        activeforeground='#eb0a1e',
                        command=lambda: set_mode('goal'))
goal_button.pack(side=tk.LEFT, padx=5)
wall_button = tk.Button(root, text="Toggle Wall",
                        font=button_font, bg='#9eb8da',
                        fg='#0c4da2', activebackground='#3d71b5',
                        activeforeground='#eb0a1e',
                        command=lambda: set_mode('wall'))
wall_button.pack(side=tk.LEFT, padx=5)
random_maze_button = tk.Button(root, text="Random Maze",
                               font=button_font, bg='#9eb8da',
                               fg='#0c4da2', activebackground='#3d71b5',
                               activeforeground='#eb0a1e',
                               command=generate_random_maze)
random_maze_button.pack(side=tk.LEFT, padx=5)
restart_button = tk.Button(root, text="Restart",
                           font=button_font, bg='#9eb8da',
                           fg='#0c4da2', activebackground='#3d71b5',
                           activeforeground='#eb0a1e', command=restart)
restart_button.pack(side=tk.RIGHT, padx=5)

root.mainloop()
