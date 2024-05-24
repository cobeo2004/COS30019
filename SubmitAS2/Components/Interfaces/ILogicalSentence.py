# Filename: ILogicalSentence.py
# Author: Simon Nguyen
# Date: 2024-04-26
# Description: Interface for converting query into Generic Propositional Form.
from Components.Interfaces.ILogic import IEvaluation


class ILogicalSentence(IEvaluation):
    """
    Interface for converting query into Generic Propositional Form.
    """

    def __init__(self, sentence) -> None:
        """Initialize the Logical Sentence with the sentence and then start formatting process.

        Args:
            - sentence (str): The sentence that we want to convert into Generic Propositional Form.
        """
        self.symbols = []  # To store the list of unique symbols of the sentence
        self.root = []  # To store the root of the processed sentence
        self.atom = {}  # To store the atomic propositions created during the formatting process
        self.original = []  # To store the original sentence split into constituent tokens

    def formatOriginal(self, sentence):
        """
        Splits the sentence into constituent tokens (operators and symbols) and store them. In addition, it also identifies unique symbols used in the sentence.

        Args:
            - sentence (str): The sentence that we want to format.
        """
        pass

    def formatSentence(self, sentence):
        """
        Format the sentence to handle expressions (unnested/nested), such as negations, conjunctions, disjunctions, implications and biconditionals, ensure sentence is splited into atomic components.

        Args:
            - sentence (list[str] extends from self.formatOriginal): The list of tokens we wanted to format.
        """
        pass

    def appendAtomic(self, index, sentence, operator):
        """
        Create atomic propositions from parts of the sentence based on the operator and updates the sentence accordingly.

        Args:
            - index (int extends from self.formatSentence): The index of the operator in the sentence
            - sentence (list[str] extends from self.formatSentence): The list of tokens representing the sentence
            - operator (str extends from self.formatSentence): The operator to process for
        """
        pass

    def evaluate(self, model):
        """
        Evaluate the sentence based on the given model, then assigns truth values to symbols.

        Args:
            model (dict[str, bool]): dictionary mapping symbols to boolean values
        """
        pass
