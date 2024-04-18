from Components.Interfaces.MapInterface import IPath, INode
from Components.Enums.Direction import Direction


class Path(IPath):
    def getFullPathFromNode(node: INode):
        if isinstance(node, INode):
            path = []
            while node:
                path.insert(0, node)
                node = node.parent
            return path
        else:
            raise ValueError(
                "node must belongs to Node class or any class that is implemented with INode")

    def reinterpretPath(path: INode, next: INode) -> str:
        if isinstance(path, INode) and isinstance(next, INode):
            if path.x < next.x:
                return Direction.RIGHT.name.lower()
            if path.x > next.x:
                return Direction.LEFT.name.lower()
            if path.y > next.y:
                return Direction.UP.name.lower()
            if path.y < next.y:
                return Direction.DOWN.name.lower()
        else:
            raise ValueError(
                "path and next must belongs to Node class or any class that is implemented with INode")
