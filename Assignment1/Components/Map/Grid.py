from Components.Interfaces.MapInterface import IGrid
from Components.Interfaces.MapInterface import INode


class Grid(IGrid):
    def __init__(self, rows: int, cols: int) -> None:
        super().__init__(rows, cols)

    def appendWall(self, x: int, y: int, w: int, h: int) -> None:
        for i in range(x, min(x + w, self.rows)):
            for j in range(y, min(y + h, self.cols)):
                self.grid[i][j] = 1

    def isMovable(self, x: int, y: int) -> bool:
        if (x >= 0 and x < self.rows) and (y >= 0 and y < self.cols) and self.grid[x][y] != 1:
            return True
        else:
            return False

    def toArray(self):
        str = ""
        for i in range(0, self.rows):
            str += f"Rows {i}: {self.grid[i]}\n"
        return str
