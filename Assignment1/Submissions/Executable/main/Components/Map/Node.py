from Components.Interfaces.MapInterface import INode

class Node(INode):
    def __init__(self, stateX, stateY, parent=None, pathCost=0) -> None:
        super().__init__(stateX, stateY, parent, pathCost)




