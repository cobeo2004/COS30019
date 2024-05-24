# Filename: main.py
# Author: Simon Nguyen and Jordan Ardley
# Date: 2024-04-18
# Description: Main file for the program. This file will read the input file and determine the type of algorithm to use.

# Import components from the Components folder and sys library for reading CLI arguments
from Components import *
import sys


def main(fileName: str, type: str):
    """Entry point of the program

    Args:
        - fileName (str): The destinaation of the file to read
        - type (str): The type of algorithm to use, which are TT, FC and BC

    Raises:
        - FileNotFoundError: Raises if file not found
        - ValueError: Rasies if no tell found
        - ValueError: Raises if no query found
        - ValueError: Raises if invalid type
    """
    try:
        # Read the file and get the tell and query
        tell, query = ReadFile().readAll(fn=fileName)
    except:
        # If the file is not found, raise an error
        raise FileNotFoundError("File not found.")

    # Throw an error if the tell and query are not found
    if len(tell) == 0:
        raise ValueError("No tell found.")
    if len(query) == 0:
        raise ValueError("No query found.")

    # Determine the type of algorithm to use
    if type.lower() == "tt":
        # Truth table
        kb = KnowledgeBase(tell, KBType.GS)
        solution = TruthTable(kb)
        print(solution.entails(query))
    elif type.lower() == "fc":
        # Forward chaining
        kb = KnowledgeBase(tell, KBType.HF)
        solution = ForwardChaining(kb)
        print(solution.entails(query))
    elif type.lower() == "bc":
        # Backward chaining
        kb = KnowledgeBase(tell, KBType.HF)
        solution = BackwardChaining(kb)
        print(solution.entails(query))
    else:
        # Throw an error if the type is not found
        raise ValueError("Invalid type.")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
