# Filename: __init__.py
# Author: Simon Nguyen and Jordan Ardley
# Date: 2024-05-20
# Description: This file will handle imports all Components from the Components folder and export it for outside usages.

# Implementations
from Components.Decorator.Export import export, all_array
from Components.Implementations.KnowledgeBase import KnowledgeBase
from Components.Implementations.LogicalSentence import LogicalSentence
from Components.Implementations.HornForm import HornForm
from Components.Implementations.ReadFile import ReadFile
from Components.Implementations.ForwardChaining import ForwardChaining
from Components.Implementations.BackwardChaining import BackwardChaining
from Components.Implementations.TruthTable import TruthTable

# Interfaces
from Components.Interfaces.ILogic import IMethod, IEvaluation
from Components.Interfaces.IHornForm import IHornForm
from Components.Interfaces.IKnowledgeBase import IKnowledgeBase
from Components.Interfaces.ILogicalSentence import ILogicalSentence
from Components.Interfaces.IReadFile import IReader
from Components.Interfaces.ITruthTable import ITruthTable
from Components.Interfaces.IForwardChaining import IForwardChaining
from Components.Interfaces.IBackwardChaining import IBackwardChaining

# Enums
from Components.Enums.KBTypes import KBType

# Export all components
__all__, __export__ = all_array, export
