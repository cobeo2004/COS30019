import os
from typing import Any


class IParse:
    def __init__(self, fileName: str) -> None:
        self._openedFile = open(fileName)

    def _parseFileName(self) -> (str | Any):
        raise NotImplementedError(
            "Method is super class and should be implemented in subclass")

    def _parseCoordinates(self, text: str) -> tuple:
        raise NotImplementedError(
            "Method is super class and should be implemented in subclass")

    def parse(self) -> list:
        raise NotImplementedError(
            "Method is super class and should be implemented in subclass")
