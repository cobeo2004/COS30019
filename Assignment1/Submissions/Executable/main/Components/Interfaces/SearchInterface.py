from typing import Any
from Components.Map.Grid import Grid


class IHeuristicType:
    """
        Interface (or could be called as parent class) for heuristic types
    """

    def __init__(self, current: tuple[int, int], goal: tuple[int, int]) -> None:
        """
        Initialize the Heuristic function class, which stores the current position and goal position

        Args:
            current (tuple[int, int]): Current position
            goal (tuple[int, int]): Goal position

        Returns:
            None: Returns nothing!
        """
        self.current = current
        self.goal = goal

    def calculate(self) -> int | float:
        """
        Calculate the value of heuristic function

        Returns:
            int | float: Returns the value of f(n) heuristic function
        """
        raise NotImplementedError(
            "Method is super class and should be implemented in subclass")

    def __add__(self, other):
        """Operator overload for adding two heuristic functions

        Args:
            other (IHeuristicType): Other heuristic function

        Returns:
            int | float: The value after adding two heuristic functions
        """
        return self.calculate() + other.calculate()


class ISearch:
    """
        Interface (or could be called as parent class) for searching algorithms,
        which includes uninformed and informed search
    """

    def __init__(self) -> None:
        """
        Initialize the Search algorithm class, which has nothing to initialize

        Returns:
            None: Returns nothing!
        """
        pass

    def search(self) -> Any:
        """Search function that should be implemented in subclass

        Args:
            self (ISearch): Is the property / method of the class

        Returns:
            Any : Returns any
        """
        raise NotImplementedError(
            "Method is super class and should be implemented in subclass")


class IUninformedSearch(ISearch):
    """
        Interface (or could be called as parent class) for uninformed searching algorithms,
        which includes uninformed and informed search
    """

    def __init__(self) -> None:
        super().__init__()

    def search(self, grid: Grid, start: tuple[int, int], goal: tuple[int, int]) -> (tuple[list, int, list] | tuple[None, int, list]):
        """Search function for the Uninformed Search

        Args:
            self (IUninformedSearch(ISearch)): Is the property / method of the class
            grid (Grid): Grid Object
            start (tuple[int,int]): Start position
            goal (tuple[int, int]): Goal position

        Returns:
            (tuple[list, int, list] | tuple[None, int, list]): Returns the path, number of nodes visited, with a collection of changes happened behind the scene
        """
        raise NotImplementedError(
            "Method is super class and should be implemented in subclass")


class IInformedSearch(ISearch):
    """
        Interface (or could be called as parent class) for informed searching algorithms,
        which includes uninformed and informed search
    """

    def __init__(self) -> None:
        super().__init__()

    def search(self, grid: Grid, start: tuple[int, int], goal: tuple[int, int],  heuristicType: IHeuristicType | int) -> (tuple[list, int, list] | tuple[None, int, list]):
        """Search function for the Informed Search

        Args:
            self (IInformedSearch(ISearch)): Is the property / method of the class
            grid (Grid): Grid Object
            start (tuple[int,int]): Start position
            goal (tuple[int, int]): Goal position
            heuristicType(IHeuristicType | int): Heuristic type

        Returns:
            (tuple[list, int, list] | tuple[None, int, list]): Returns the path, number of nodes visited, with a collection of changes happened behind the scene
        """
        raise NotImplementedError(
            "Method is super class and should be implemented in subclass")
