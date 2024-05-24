# Filename: KBTypes.py
# Author: Jordan Ardley
# Date: 2024-05-02
# Description: Enumerator for which type of Knowledge Base Sentence to use

from enum import Enum
from Components.Decorator.Export import export


@export
class KBType(Enum):
    """
        Enumerator for which type of Knowledge Base sentence to use

        Properties:
            - HF = 1: Horn Form
            - GS = 2: Generic Propositional Form

        Methods:
            - @static getKBType(type: str) -> KBType: Get type based on the string type
            - @static isKBType(type: KBType?) -> bool: Check if the given type is in enumaration properties

    """
    HF = 1
    GS = 2

    @staticmethod
    def getKBType(type: str):
        if type.lower() == 'hf':
            return KBType.HF
        elif type.lower() == 'gs':
            return KBType.GS
        else:
            raise Exception("Unknown sentence type.")

    @staticmethod
    def isKBType(type):
        if type is KBType.HF or type is KBType.GS:
            return True
        return False
