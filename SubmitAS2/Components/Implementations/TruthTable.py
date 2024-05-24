from Components.Decorator.Export import export
from Components.Implementations.LogicalSentence import LogicalSentence
from Components.Interfaces.ITruthTable import ITruthTable


@export
class TruthTable(ITruthTable):
    def __init__(self, knowledgeBase):
        ###########
        # ITruthTable initializer
        # self.knowledgeBase = knowledgeBase
        # self.count = 0
        ###########
        super().__init__(knowledgeBase)

    def __check(self, alphabetic, symbols, model):
        # Base case: if there are no more symbols to evaluate
        if len(symbols) == 0:
            all_eval = True  # Assume all sentences in the knowledge base evaluate to True
            for sentence in self.knowledgeBase.sentences:
                # Evaluate each sentence with the current model
                if not sentence.evaluate(model):
                    all_eval = False  # If any sentence evaluates to False, set all_eval to False
            if all_eval:
                # Evaluate the query with the current model
                alpha = alphabetic.evaluate(model)
                if alpha:
                    self.count += 1  # Increment the count if the query evaluates to True
                return alpha  # Return the evaluation of the query
            else:
                return True  # If not all sentences in the knowledge base evaluate to True, return True
        else:
            firstSymbol = symbols[0]  # Get the first symbol
            restSymbol = symbols[1:]  # Get the rest of the symbols
            model1 = model.copy()  # Copy the current model
            # Set the first symbol to True in the copied model
            model1.update({firstSymbol: True})
            model2 = model.copy()  # Copy the current model again
            # Set the first symbol to False in the copied model
            model2.update({firstSymbol: False})
            # Recursively check the rest of the symbols with both models
            return (self.__check(alphabetic, restSymbol, model1) and self.__check(alphabetic, restSymbol, model2))

    def __truth_table(self, alphabetic):
        symbols = self.knowledgeBase.symbols  # Get the symbols from the knowledge base
        for symbol in alphabetic.symbols:
            if symbol not in symbols:  # Add symbols from the query if they are not already in the knowledge base
                symbols.append(symbol)
        # Start the truth table check with an empty model
        return self.__check(alphabetic, symbols, {})

    def entails(self, query):
        # Create a LogicalSentence object for the query
        alpha = LogicalSentence(query)
        # Generate the truth table for the query
        solution = self.__truth_table(alpha)
        if solution:
            # If the query is entailed, return "YES" with the count
            result = "YES: " + str(self.count)
        else:
            result = "NO"  # If the query is not entailed, return "NO"
        return result  # Return the result
