# Filename: IForwardChaining.py
# Author: Simon Nguyen
# Date: 2024-04-26
# Description: Interface for forward chaining algorithm.

from Components.Interfaces.ILogic import IMethod


class IForwardChaining(IMethod):
    """
    Forward Chaining algorithm interface
    """

    def __init__(self, knowledgeBase) -> None:
        """Initialize of Forward Chaining algorithm.
        Args:
            - knowledgeBase (IKnowledgeBase<IHornForm>): Knowledge base that algorithm will use, which must be Horn Form.
        """
        self.knowledgeBase = knowledgeBase  # The knowledge base that alogrithm will use
        self.count = {}  # To keep track of count of symbols in the knowledge base
        self.inferred = {}  # To keep track of already inferred symbols
        self.agenda = []  # To keep the agenda of symbols to be inferred
        self.chain = []  # To keep the chain of inferences

    def __forward_chaining(self, query):
        """ The main implemenation of forward chaining algorithm
        Args:
            - query (str): The query that we want to prove.

        Return:
            - bool: If proven then return True, otherwise False.
        """
        pass

    def entails(self, query):
        """ Entails method that returns if the query could be proven or not, base on calling the underlying __forward_chaining.

        Args:
            - query (str): The query that we want to prove.

        Return:
            - str: If proven then return with YES + the chain of inferrence, otherwise NO.
        """
        pass
