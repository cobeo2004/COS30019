from enum import Enum


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @staticmethod
    def getTupleValues():
        return [(0, -1), (0, 1), (-1, 0), (1, 0)]
