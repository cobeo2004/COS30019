from Components.Map.Grid import Grid
from Components.Searchers.Heuristic import ManhattanDistance
from Components.Searchers.Informed import AStarSearch, CustomSearchTwo, GreedyBestFirstSearch
from Components.Searchers.Uninformed import BreadthFirstSearch, CustomSearchOne, DepthFirstSearch


class Searcher:
    def __init__(self, grid: Grid, start: tuple[int, int], goal: list[tuple[int, int]], typeOfSearch: str) -> None:
        self.grid = grid
        self.start = start
        self.goal = goal
        self.typeOfSearch = typeOfSearch
        self.heuristicFunction = ManhattanDistance
        self.tPath, self.numNodes, self.changes = [], [], []

    def getResult(self):
        if type(self.goal) is list:
            for i in range(len(self.goal)):
                if self.typeOfSearch.lower() == "dfs":
                    path, numberOfNodes, changes = DepthFirstSearch().search(
                        self.grid, self.start, self.goal[i])
                elif self.typeOfSearch.lower() == "bfs":
                    path, numberOfNodes, changes = BreadthFirstSearch().search(
                        self.grid, self.start, self.goal[i])
                elif self.typeOfSearch.lower() == "cus1":
                    path, numberOfNodes, changes = CustomSearchOne().search(self.grid,
                                                                            self.start, self.goal[i])
                elif self.typeOfSearch.lower() == "gbfs":
                    path, numberOfNodes, changes = GreedyBestFirstSearch().search(
                        self.grid, self.start, self.goal[i], self.heuristicFunction)
                elif self.typeOfSearch.lower() == "as":
                    path, numberOfNodes, changes = AStarSearch().search(
                        self.grid, self.start, self.goal[i], self.heuristicFunction)

                elif self.typeOfSearch.lower() == "cus2":
                    path, numberOfNodes, changes = CustomSearchTwo().search(
                        self.grid, self.start, self.goal[i], self.heuristicFunction)
                else:
                    raise ValueError(
                        "Please provide a valid search algorithm [bfs, dfs, as, gbfs, cus1, cus2]")
                self.tPath.append(path)
                self.numNodes.append(numberOfNodes)
                self.changes.append(changes)
            if (self.typeOfSearch.lower() in ["bfs", "dfs", "cus1"]):
                return self.tPath, self.numNodes, self.changes
            else:
                i = 0
                while i < len(self.tPath):
                    if len(self.tPath[i]) <= len(self.tPath[i + 1]):
                        return [self.tPath[i]], self.numNodes[i], self.changes[i]
                    i += 1

        if type(self.goal) is tuple:
            if self.typeOfSearch.lower() == "dfs":
                path, numberOfNodes, changes = DepthFirstSearch().search(
                    self.grid, self.start, self.goal)
            elif self.typeOfSearch.lower() == "bfs":
                path, numberOfNodes, changes = BreadthFirstSearch().search(
                    self.grid, self.start, self.goal)
            elif self.typeOfSearch.lower() == "cus1":
                path, numberOfNodes, changes = CustomSearchOne().search(self.grid,
                                                                        self.start, self.goal)
            elif self.typeOfSearch.lower() == "gbfs":
                path, numberOfNodes, changes = GreedyBestFirstSearch().search(
                    self.grid, self.start, self.goal, self.heuristicFunction)
            elif self.typeOfSearch.lower() == "as":
                path, numberOfNodes, changes = AStarSearch().search(
                    self.grid, self.start, self.goal, self.heuristicFunction)

            elif self.typeOfSearch.lower() == "cus2":
                path, numberOfNodes, changes = CustomSearchTwo().search(
                    self.grid, self.start, self.goal, self.heuristicFunction)
            else:
                raise ValueError(
                    "Please provide a valid search algorithm [bfs, dfs, as, gbfs, cus1, cus2]")

            return path, numberOfNodes, changes
