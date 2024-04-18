from Components.Map.Node import Node
from Components.Map.Grid import Grid
from Components.Enums.Direction import Direction
from Components.Searchers.Heuristic import Heuristic
import heapq
from Components.Map.Path import Path
from Components.Interfaces.SearchInterface import IHeuristicType, IInformedSearch


class GreedyBestFirstSearch(IInformedSearch):
    def search(self, grid: Grid, start: tuple[int, int], goal: tuple[int, int], heuristicType: IHeuristicType | int) -> (tuple[list, int, list] | tuple[None, int, list]):
        if issubclass(heuristicType, IHeuristicType):
            nodeCost = heuristicType(start, goal).calculate()
        else:
            nodeCost = Heuristic(
                start, goal).getHeuristicFunction(heuristicType)
        frontierQueue = [(nodeCost, Node(start[0], start[1]))]
        heapq.heapify(frontierQueue)
        visitedNodes = set()
        changes = []
        countedNodes = 0
        while frontierQueue:
            cost, node = heapq.heappop(frontierQueue)
            countedNodes += 1
            if (node.x, node.y) == goal:
                return Path.getFullPathFromNode(node), countedNodes, changes
            visitedNodes.add((node.x, node.y))
            changes.append(((node.x, node.y), 'visited'))
            for directionX, directionY in Direction.getTupleValues():
                nextX, nextY = directionX + node.x, directionY + node.y
                if (nextX, nextY) not in visitedNodes and grid.isMovable(nextX, nextY):
                    childNode = Node(nextX, nextY, node, node.pathCost + 1)
                    if issubclass(heuristicType, IHeuristicType):
                        nodeCost = heuristicType(
                            (nextX, nextY), goal).calculate()
                    else:
                        nodeCost = Heuristic(
                            start, goal).getHeuristicFunction(heuristicType)
                    heapq.heappush(frontierQueue, (nodeCost, childNode))
                    visitedNodes.add((nextX, nextY))
                    changes.append(((nextX, nextY), 'frontier'))
        return None, countedNodes, changes


class AStarSearch(IInformedSearch):
    def search(self, grid: Grid, start: tuple[int, int], goal: tuple[int, int], heuristicType: IHeuristicType | int) -> (tuple[list, int, list] | tuple[None, int, list]):
        if issubclass(heuristicType, IHeuristicType):
            nodeCost = heuristicType(start, goal).calculate()
        else:
            nodeCost = Heuristic(
                start, goal).getHeuristicFunction(heuristicType)

        frontierQueue = [(nodeCost, Node(start[0], start[1]))]
        heapq.heapify(frontierQueue)
        visitedNodes = set()
        countedNodes = 0
        changes = []
        while frontierQueue:
            cost, node = heapq.heappop(frontierQueue)
            countedNodes += 1
            if (node.x, node.y) == goal:
                return Path.getFullPathFromNode(node), countedNodes, changes

            visitedNodes.add((node.x, node.y))
            changes.append(((node.x, node.y), 'visited'))
            for directionX, directionY in Direction.getTupleValues():
                nextX, nextY = directionX + node.x, directionY + node.y
                if (nextX, nextY) not in visitedNodes and grid.isMovable(nextX, nextY):
                    childNode = Node(nextX, nextY, node, node.pathCost + 1)
                    if issubclass(heuristicType, IHeuristicType):
                        nodeCost = heuristicType(start, goal).calculate(
                        ) + heuristicType((nextX, nextY), goal).calculate()
                    else:
                        nodeCost = Heuristic(start, (nextX, nextY)).getHeuristicFunction(
                            heuristicType) + Heuristic((nextX, nextY), goal).getHeuristicFunction(heuristicType)
                    heapq.heappush(frontierQueue, (nodeCost, childNode))
                    visitedNodes.add((nextX, nextY))
                    changes.append(((nextX, nextY), 'frontier'))
        return None, countedNodes, changes


class CustomSearchTwo(IInformedSearch):

    def search(self, grid: Grid, start: tuple[int, int], goal: tuple[int, int], heuristicType: IHeuristicType | int, weight: int = 0):

        if weight == 0:
            _weight = 1.25
        else:
            _weight = weight

        result, nodeCount, changes = self._weightedAStarSearch(
            grid, start, goal, heuristicType, _weight)

        return result, nodeCount, changes

    def _weightedAStarSearch(self, grid: Grid, start: tuple[int, int], goal: tuple[int, int], heuristicType: IHeuristicType | int, weight: float):
        start_node = Node(start[0], start[1], None, 0)

        if issubclass(heuristicType, IHeuristicType):
            start_heuristic = heuristicType(start, goal).calculate()
        else:
            start_heuristic = Heuristic(
                start, goal).getHeuristicFunction(heuristicType)

        start_cost = start_node.pathCost + weight * start_heuristic
        frontierQueue = [(start_cost, start_node)]
        heapq.heapify(frontierQueue)

        visitedNodes = set()
        countedNodes = 0
        changes = []

        while frontierQueue:
            current_cost, node = heapq.heappop(frontierQueue)
            countedNodes += 1

            if (node.x, node.y) == goal:
                return Path.getFullPathFromNode(node), countedNodes, changes

            visitedNodes.add((node.x, node.y))
            changes.append(((node.x, node.y), 'visited'))

            for directionX, directionY in Direction.getTupleValues():
                nextX, nextY = node.x + directionX, node.y + directionY
                if (nextX, nextY) not in visitedNodes and grid.isMovable(nextX, nextY):
                    childNode = Node(nextX, nextY, node, node.pathCost + 1)
                    if issubclass(heuristicType, IHeuristicType):
                        child_heuristic = heuristicType(
                            (nextX, nextY), goal).calculate()
                    else:
                        child_heuristic = Heuristic(
                            (nextX, nextY), goal).getHeuristicFunction(heuristicType)

                    # Apply the weighting factor only to the heuristic component
                    child_cost = childNode.pathCost + weight * child_heuristic
                    heapq.heappush(frontierQueue, (child_cost, childNode))
                    visitedNodes.add((nextX, nextY))
                    changes.append(((nextX, nextY), 'frontier'))

        return None, countedNodes, changes
