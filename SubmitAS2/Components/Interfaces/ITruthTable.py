# Filename: ITruthTable.py
# Author: Jordan Ardley
# Date: 2024-04-29
# Description: Interface for Truth Table implementation.

# Import the IMethod interface
from Components.Interfaces.ILogic import IMethod


class ITruthTable(IMethod):
    """Truth table algorithm interface
    """

    def __init__(self, knowledgeBase):
        """Initialise the Truth Table algorithm

        Args:
            - knowledgeBase (ILogicalSentence): The knowledge base that alogrithm will use, which is Generic Knowledge Base sentence.
        """
        self.knowledgeBase = knowledgeBase
        self.count = 0

    def __truth_table(self, alphabetic):
        pass

    def __check(self, alphabetic, symbols, model):
        pass

    def entails(self, query):
        pass
