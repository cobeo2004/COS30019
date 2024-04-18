from enum import Enum

class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 255, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PURPLE = (128, 0, 128)
    ORANGE = (255, 165 ,0)
    GREY = (128, 128, 128)
    TURQUOISE = (64, 224, 208)

    @classmethod
    def getColor(cls, name: str) -> tuple[int, int ,int]:
        for color in cls:
            if color.name == name.upper():
                return color.value
        raise ValueError(f"Invalid color name: {name}")
