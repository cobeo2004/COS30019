from Components.Interfaces.IForwardChaining import IForwardChaining
from Components.Decorator.Export import export


@export
class ForwardChaining(IForwardChaining):
    def __init__(self, knowledgeBase) -> None:
        ###########
        # IForwardChaining initializer
        # self.count = {}  # To keep track of count of symbols in the knowledge base
        # self.inferred = {}  # To keep track of already inferred symbols
        # self.agenda = []  # To keep the agenda of symbols to be inferred
        # self.chain = []  # To keep the chain of inferences
        ###########
        super().__init__(knowledgeBase)

    def __forward_chaining(self, query):
        # Clear the chain at the beginning of the forward chaining process
        self.chain.clear()

        # Initialize agenda with facts and count conjuncts for each sentence in the knowledge base
        for sentence in self.knowledgeBase.sentences:
            if len(sentence.conjuncts) == 0:
                # If the sentence is a fact (no conjuncts)
                if sentence.head == query:
                    # If the fact matches the query, add to the chain and return True
                    self.chain.append(query)
                    return True
                # Add the fact to the agenda
                self.agenda.append(sentence.head)
            else:
                # Initialize count of conjuncts for each rule
                self.count.update({sentence: len(sentence.conjuncts)})

        # Initialize inferred status for each symbol in the knowledge base
        for symbol in self.knowledgeBase.symbols:
            self.inferred.update({symbol: False})

        # Process symbols in the agenda
        while len(self.agenda) != 0:
            p = self.agenda.pop(0)
            if not self.inferred[p]:
                # Mark the symbol as inferred and add to the chain
                self.chain.append(p)
                self.inferred[p] = True
                for sentence in self.count:
                    if p in sentence.conjuncts:
                        # Decrement the count of conjuncts for the rules containing p
                        self.count[sentence] -= 1
                        if self.count[sentence] == 0:
                            # If all conjuncts of a rule are inferred
                            if sentence.head == query:
                                # If the rule's head matches the query, add to the chain and return True
                                self.chain.append(sentence.head)
                                return True
                            # Add the rule's head to the agenda
                            self.agenda.append(sentence.head)

        # If the query cannot be inferred, return False
        return False

    def entails(self, query):
        # Start the forward chaining process to determine if the query can be inferred
        isFound = self.__forward_chaining(query)

        # Format the result based on whether the query can be inferred or not
        if isFound:
            result = "YES: " + ", ".join(self.chain)
        else:
            result = "NO"

        # Return the result
        return result
