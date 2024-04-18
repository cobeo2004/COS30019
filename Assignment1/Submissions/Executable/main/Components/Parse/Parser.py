from io import *
import os
from Components.Interfaces.ParseInterface import IParse


class Parser(IParse):
    def __init__(self, fileName: str) -> None:
        super().__init__(fileName)

    def _parseFileName(self):
        return os.path.basename(self._openedFile.name)

    def _parseCoordinates(self, text: str):
        self._t = text.strip('[]()\n')
        return tuple(map(int, self._t.split(',')))

    def parse(self) -> list:
        self._lines = self._openedFile.readlines()
        self._dimensions = self._parseCoordinates(self._lines[0])
        self._startLocation = self._parseCoordinates(self._lines[1])[::1]
        self._goalStates = [self._parseCoordinates(
            g.strip())[::1] for g in self._lines[2].split("|")]
        self._walls = [self._parseCoordinates(
            line) for line in self._lines[3:]]
        return {
            "fileName": self._parseFileName(),
            "gridSize": self._dimensions,
            "startLocation": self._startLocation,
            "goalLocation": self._goalStates,
            "walls": self._walls
        }
