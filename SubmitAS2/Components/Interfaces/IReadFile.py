# Filename: IReadFile.py
# Author: Jordan Ardley
# Date: 2024-04-24
# Description: Interface for reading files
class IReader:
    """
    Interface for reading files
    """

    def readAll(self, fn: str) -> tuple[list[str], str]:
        """Read all function to read both the tell and ask query

        Args:
            fn (str): The file name to read

        Returns:
            tuple[list[str], str]: The tell and ask query
        """
        pass
