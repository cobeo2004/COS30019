# Filename: ILogic.py
# Author: Simon Nguyen
# Date: 2024-05-24
# Description: Template interface for every logical sub-interface implementation.

class IEvaluation:
    """
    Main interface / or could be treated as a template for all logical sentences.
    """

    def __init__(self) -> None:
        """
            Constructor for IEvaluation, depends on the sub-classes.
        """
        pass

    def evaluate(self):
        """
            Evaluate the logical sentence.
        """
        pass


class IMethod:
    """
    Main interface / or could be treated as a template for all Knowledge Base algortithms.
    """

    def __init__(self) -> None:
        """
        Constructor for IMethod, depends on the sub-classes.
        """
        pass

    def entails(self):
        """
        Check if the query is entailed by the knowledge base.
        """
        pass
