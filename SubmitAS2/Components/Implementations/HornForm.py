from Components.Interfaces.IHornForm import IHornForm
from Components.Decorator.Export import export
import re


@export
class HornForm(IHornForm):
    def __init__(self, sentence) -> None:
        ######
        # IHornForm initializer
        # self.clauses = []  # To keep the clauses of the sentence
        # self.symbols = set()  # Use a set to avoid duplicates
        # self.sentence = sentence  # The sentence that we want to convert into Horn Form
        # self.head = ""  # The head of the sentence
        # self.conjuncts = []  # The conjuncts of the sentence
        ######
        super().__init__(sentence)
        # Evaluate the given sentence to convert it into Horn form
        self.evaluate()

    def evaluate(self):
        # Split the sentence into clauses based on logical operators and parentheses
        self.clauses = re.split("(=>|&|\(|\)|~|\|\||<=>)", self.sentence)
        # Strip whitespace and filter out empty strings and parentheses from the clauses
        self.clauses = [c.strip()
                        for c in self.clauses if c.strip() and c not in "()"]

        # Check if the sentence contains any operators that are not allowed in Horn form
        if any(op in self.clauses for op in ['~', '||', '<=>']):
            # Raise an error if the sentence is not in Horn form
            raise ValueError("Sentence is not in horn form", self.clauses)

        # If the sentence is a fact (only one clause)
        if len(self.clauses) == 1:
            self.head = self.clauses[0]
            self.symbols.add(self.head)
        else:
            # Find the index of the implication operator
            index = self.clauses.index('=>')
            # Get the right-hand side (head) of the implication
            rhs = self.clauses[index + 1:]
            if len(rhs) > 1:
                # Raise an error if the right-hand side is not a single symbol
                raise ValueError("Error horn form format", self.clauses)
            self.head = rhs[0]
            self.symbols.add(self.head)

            # Get the left-hand side (body) of the implication
            lhs = self.clauses[:index]
            if lhs[0] == '&' or lhs[-1] == '&':
                # Raise an error if the body starts or ends with a conjunction operator
                raise ValueError("Error horn form format", self.clauses)

            # Check for consecutive conjunction operators
            for i in range(len(lhs) - 1):
                if lhs[i] == '&' and lhs[i + 1] == '&':
                    # Raise an error if there are consecutive conjunction operators
                    raise ValueError("Error horn form format", self.clauses)
            for value in lhs:
                if value != '&':
                    # Add each symbol in the body to the list of conjuncts and symbols
                    self.conjuncts.append(value)
                    self.symbols.add(value)

        # Convert the set of symbols back to a list for the final output
        self.symbols = list(self.symbols)
