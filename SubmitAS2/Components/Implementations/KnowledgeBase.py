from Components.Interfaces.IKnowledgeBase import IKnowledgeBase
from Components.Decorator.Export import export
from Components.Enums.KBTypes import KBType
from Components.Implementations.LogicalSentence import LogicalSentence
from Components.Implementations.HornForm import HornForm


@export
class KnowledgeBase(IKnowledgeBase):
    def __init__(self, sentences, type: KBType) -> None:
        # Initialize an empty list to store sentences and symbols
        self.sentences = []
        self.symbols = []

        # Validate and set the knowledge base type
        if KBType.isKBType(type):
            self.type = type
        else:
            # Raise an error if the knowledge base type is invalid
            raise ValueError("Unknown knowledge base type.")

        # Process each sentence in the provided list of sentences
        for value in sentences:
            self.queryAsk(value)

    def queryAsk(self, sentence):
        # Create a new sentence object based on the knowledge base type
        if self.type == KBType.GS:
            newSentence = LogicalSentence(sentence)
        elif self.type == KBType.HF:
            newSentence = HornForm(sentence)

        # Add the new sentence to the list of sentences in the knowledge base
        self.sentences.append(newSentence)

        # Add any new symbols from the sentence to the symbols list
        for value in newSentence.symbols:
            if value not in self.symbols:
                self.symbols.append(value)
