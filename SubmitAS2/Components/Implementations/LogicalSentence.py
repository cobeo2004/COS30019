from Components.Interfaces.ILogicalSentence import ILogicalSentence
from Components.Decorator.Export import export
import re


@export
class LogicalSentence(ILogicalSentence):
    def __init__(self, sentence) -> None:
        #######
        # ILogicalSentence initializer
        # self.symbols = []  # To store the list of unique symbols of the sentence
        # self.root = []  # To store the root of the processed sentence
        # self.atom = {}  # To store the atomic propositions created during the formatting process
        # self.original = []  # To store the original sentence split into constituent tokens
        #######
        super().__init__(sentence)
        # Format the original sentence upon initialization
        self.formatOriginal(sentence)

    def formatOriginal(self, sentence):
        # Split the sentence into tokens using logical operators and parentheses as delimiters
        orig = re.split("(=>|&|\(|\)|~|\|\||<=>)", sentence)
        # Remove any empty strings from the list of tokens
        while "" in orig:
            orig.remove("")
        # Strip whitespace from each token and store the cleaned tokens in self.original
        self.original = [token.strip() for token in orig if token.strip()]
        # Split the sentence to extract symbols using only logical operators as delimiters
        symbols = re.split("=>|&|\(|\)|~|\|\||<=>", sentence)
        # Remove any empty strings from the list of symbols
        while "" in symbols:
            symbols.remove("")
        # Store unique symbols in self.symbols
        self.symbols = list(set(symbols))
        # Format the sentence to identify atomic propositions and its structure
        self.root = self.formatSentence(orig)

    def formatSentence(self, sentence):
        # Handle nested expressions within parentheses
        while '(' in sentence:
            # Find the index of the first opening parenthesis
            lhsIndex = sentence.index('(')
            countLeft = 1  # Initialize count of left parentheses
            countRight = 0  # Initialize count of right parentheses
            rhsIndex = 0  # Initialize the index for the matching closing parenthesis

            # Find the matching closing parenthesis for the first opening parenthesis
            for i in range(lhsIndex + 1, len(sentence)):
                if sentence[i] == '(':
                    countLeft += 1  # Increment count of left parentheses
                elif sentence[i] == ')':
                    countRight += 1  # Increment count of right parentheses
                if countLeft == countRight:
                    rhsIndex = i  # Set the index of the matching closing parenthesis
                    break
            # Raise an error if no matching closing parenthesis is found
            if rhsIndex == 0:
                raise ValueError(
                    "Incorrect brackets format in sentence: ", sentence)
            # Recursively format the nested section
            section = sentence[lhsIndex + 1: rhsIndex]
            section = self.formatSentence(section)
            # If the nested section is a single token, replace the parentheses with the token
            if len(section) == 1:
                sentence[lhsIndex] = section[0]
                del sentence[lhsIndex + 1: rhsIndex + 1]
            else:
                raise ValueError("Incorrect section format: ", section)

        # Process negation operators
        while '~' in sentence:
            # Find the index of the negation operator
            index = sentence.index('~')
            # Process the negation operator
            sentence = self.appendAtomic(index, sentence, '~')

        # Process conjunction and disjunction operators
        while '&' in sentence or '||' in sentence:
            if '&' in sentence and ('||' not in sentence or sentence.index('&') < sentence.index('||')):
                # Find the index of the conjunction operator
                index = sentence.index('&')
            elif '||' in sentence:
                # Find the index of the disjunction operator
                index = sentence.index('||')
            else:
                break
            # Process the conjunction or disjunction operator
            sentence = self.appendAtomic(index, sentence, '&||')

        # Process implication operators
        while '=>' in sentence:
            # Find the index of the implication operator
            index = sentence.index('=>')
            # Process the implication operator
            sentence = self.appendAtomic(index, sentence, '=>')

        # Process biconditional operators
        while '<=>' in sentence:
            # Find the index of the biconditional operator
            index = sentence.index('<=>')
            # Process the biconditional operator
            sentence = self.appendAtomic(index, sentence, '<=>')

        return sentence  # Return the formatted sentence

    def appendAtomic(self, index, sentence, operator):
        if operator == '~':
            # Handle negation operator
            # Create an atomic proposition for negation
            tempAtomic = [sentence[index], sentence[index + 1]]
            # Generate a unique key for the atomic proposition
            tempAtomicKey = "atom" + str(len(self.atom) + 1)
            # Add the atomic proposition to self.atom
            self.atom.update({tempAtomicKey: tempAtomic})
            # Replace the operator and its operand with the atomic proposition key
            sentence[index] = tempAtomicKey
            del sentence[index + 1]  # Remove the operand from the sentence
        else:
            # Handle binary operators (conjunction, disjunction, implication, biconditional)
            # Create an atomic proposition for binary operators
            tempAtomic = [sentence[index - 1],
                          sentence[index], sentence[index + 1]]
            # Generate a unique key for the atomic proposition
            tempAtomicKey = "atom" + str(len(self.atom) + 1)
            # Add the atomic proposition to self.atom
            self.atom.update({tempAtomicKey: tempAtomic})
            # Replace the operands and operator with the atomic proposition key
            sentence[index - 1] = tempAtomicKey
            # Remove the operands and operator from the sentence
            del sentence[index:index + 2]
        return sentence  # Return the updated sentence

    def evaluate(self, model):
        # Create a dictionary to map symbols to their boolean values from the provided model
        bool_pairs = {}
        for value in self.symbols:
            if value in model:
                # Add the symbol and its boolean value to bool_pairs
                bool_pairs.update({value: model[value]})
            else:
                # Raise an error if a symbol does not have a boolean value in the model
                raise ValueError("No boolean for all symbols.")

        # Evaluate each atomic proposition based on the logical operator
        for key in self.atom:
            if len(self.atom[key]) == 2:
                # Evaluate negation
                # Get the boolean value of the operand
                right = bool_pairs[self.atom[key][1]]
                # Negate the boolean value and update bool_pairs
                bool_pairs.update({key: not right})
            elif len(self.atom[key]) == 3:
                # Get the boolean value of the left operand
                left = bool_pairs[self.atom[key][0]]
                # Get the boolean value of the right operand
                right = bool_pairs[self.atom[key][2]]
                if self.atom[key][1] == '&':
                    # Evaluate conjunction
                    bool_pairs.update({key: left and right})
                elif self.atom[key][1] == '||':
                    # Evaluate disjunction
                    bool_pairs.update({key: left or right})
                elif self.atom[key][1] == '=>':
                    # Evaluate implication
                    bool_pairs.update({key: not left or right})
                elif self.atom[key][1] == '<=>':
                    # Evaluate biconditional
                    bool_pairs.update({key: left == right})
            else:
                # Raise an error if an atomic proposition is not in the correct format
                raise ValueError(
                    "Atomic sentence in incorrect format: ", self.atom[key])

        # Return the boolean value of the root of the sentence
        return bool_pairs[self.root[0]]
