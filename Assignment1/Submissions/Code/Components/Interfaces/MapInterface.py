class IGrid:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * cols for _ in range(rows)]

    def appendWall(self, x: int, y: int, w: int, h: int) -> None:
        raise NotImplementedError("Method should be implemented in base class")

    def isMovable(self, x: int, y: int) -> bool:
        raise NotImplementedError("Method should be implemented in base class")

    def toArray(self):
        raise NotImplementedError("Method should be implemented in base class")


class INode:
    def __init__(self, sX: int, sY: int, parent=None, pathCost: int = 0) -> None:
        self.x = sX
        self.y = sY
        self.parent = parent
        self.pathCost = pathCost
        self.depth = 0

    def __repr__(self) -> str:
        return f"<Node ({self.x}, {self.y})>"

    def __lt__(self, node: object):
        return (self.x + self.y) < (node.x + node.y) if isinstance(node, INode) else False

    def __eq__(self, node: object) -> bool:
        return (self.x + self.y) == (node.x + node.y) if isinstance(node, INode) else False


class IPath:
    def __init__(self) -> None:
        pass

    def getFullPathFromNode(self, node: INode) -> list:
        raise NotImplementedError("Method should be implemented in base class")

    def reinterpretPath(self, path: INode, next: INode) -> str:
        raise NotImplementedError("Method should be implemented in base class")
