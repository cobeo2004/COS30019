# Filename: IknowledgeBase.py
# Author: Simon Nguyen
# Date: 2024-04-25
# Description: Interface for Knowledge base.
from Components.Enums.KBTypes import KBType


class IKnowledgeBase:
    """
        Knowledge Base interface, which is use for determine which kind of knowledge base form to use
    """

    def __init__(self, sentences, type: KBType) -> None:
        """Initialize the knowledge base with the sentences and type of knowledge base.

        Args:
            sentences (list[str]): list of splited (not parsed) tells.
            type (KBType): The type of knowledge base.
        """
        pass

    def queryAsk(self, sentence):
        """Query the knowledge base with the sentence.

        Args:
            sentence (str): Unparsed sentence.
        """
        pass
