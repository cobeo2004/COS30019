# Filename: IHornForm.py
# Author: Jordan Ardley
# Date: 2024-04-26
# Description: Interface for converting query into Horn Form.

from Components.Interfaces.ILogic import IEvaluation


class IHornForm(IEvaluation):
    """
    Horn Form converter interface
    """

    def __init__(self, sentence) -> None:
        """Initialize of Horn Form converter.

        Args:
            - sentence (str): The sentence that we want to convert into Horn Form.
        """
        self.clauses = []  # To keep the clauses of the sentence
        self.symbols = set()  # Use a set to avoid duplicates
        self.sentence = sentence  # The sentence that we want to convert into Horn Form
        self.head = ""  # The head of the sentence
        self.conjuncts = []  # The conjuncts of the sentence

    def evaluate(self):
        """
        Evaluate the sentence and convert it into Horn Form
        """
        pass
