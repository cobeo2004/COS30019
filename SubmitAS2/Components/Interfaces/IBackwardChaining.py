# Filename: IBackwardChaining.py
# Author: Simon Nguyen
# Date: 2024-04-26
# Description: Interface for backward chaining algorithm.

from Components.Interfaces.ILogic import IMethod
from Components.Interfaces.IKnowledgeBase import IKnowledgeBase


class IBackwardChaining(IMethod):
    """
    Backward Chaining algorithm interface
    """

    def __init__(self, knowledgeBase: IKnowledgeBase) -> None:
        """Initialize of Backward Chaining algorithm.
        Args:
            - knowledgeBase (IKnowledgeBase<IHornForm>): Knowledge base that algorithm will use, which must be Horn Form.
        """
        self.knowledgeBase = knowledgeBase  # The knowledge base that alogrithm will use
        self.inferred = set()  # To keep track of already inferred symbols
        self.chain = []  # To keep the chain of inferences
        self.visited = set()  # To keep track of visited nodes to detect circular dependencies

    def __backward_chaining(self, query):
        """ The main implemenation of backward chaining algorithm, which is recursive.
        Args:
            - query (str): The query that we want to prove.

        Return:
            - bool: If proven then return True, otherwise False.
        """
        pass

    def entails(self, query):
        """ Entails method that returns if the query could be proven or not, base on calling the underlying __backward_chaining.

        Args:
            - query (str): The query that we want to prove.

        Return:
            - str: If proven then return with YES + the chain of inferrence, otherwise NO.
        """
        pass
