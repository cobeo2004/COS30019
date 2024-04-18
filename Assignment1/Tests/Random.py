from random import randint

class GenerateRandomTexture:
    def __init__(self, sizeOfRows: int, sizeOfCols: int, numOfWalls: int = 2, numOfGoals: int = 1) -> None:
        self._grid = [sizeOfRows, sizeOfCols]
        self._startPoint = (randint(0, sizeOfRows), randint(0, sizeOfCols))
        self._endPoint = [(randint(0, sizeOfRows), randint(0, sizeOfCols)) for _ in range(numOfGoals)]
        self._walls = [(randint(0, sizeOfRows), randint(0, sizeOfCols), 1, 1) for _ in range(numOfWalls)]

    def getAll(self):
        return {
            "gridSize": self._grid,
            "startLocation": self._startPoint,
            "goalLocation": self._endPoint,
            "walls": self._walls
        }

    def toText(self):
        with open("random.txt", "w") as f:
            f.write(f"[{self._grid[0]},{self._grid[1]}]\n")
            f.write(f"({self._startPoint[0]},{self._startPoint[1]})\n")
            f.write(" | ".join([f"({goal[0]},{goal[1]})" for goal in self._endPoint]) + "\n")
            f.write("\n".join([f"({wall[0]},{wall[1]},{wall[2]},{wall[3]})" for wall in self._walls]))

if __name__ == "__main__":
    g = GenerateRandomTexture(40, 40, 13, 10)
    print(g.getAll())
    print(g.toText())

