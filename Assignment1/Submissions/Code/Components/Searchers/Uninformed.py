from Components.Map.Node import Node
from Components.Map.Grid import Grid
from collections import deque
from Components.Enums.Direction import Direction
from Components.Map.Path import Path
from Components.Interfaces.SearchInterface import IUninformedSearch


class DepthFirstSearch(IUninformedSearch):

    def search(self, grid: Grid, start: tuple[int, int], goal: tuple[int, int]):
        frontierStack = [(Node(start[0], start[1]), [])]
        countedNodes = 0
        visitedNodes = set()
        changes = []
        while frontierStack:
            node, _ = frontierStack.pop()
            countedNodes += 1
            if (node.x, node.y) == goal:
                return Path.getFullPathFromNode(node), countedNodes, changes
            visitedNodes.add((node.x, node.y))
            changes.append(((node.x, node.y), 'visited'))

            unvisitedNodes = []
            for directionX, directionY in Direction.getTupleValues():
                nextX, nextY = directionX + node.x, directionY + node.y
                if (nextX, nextY) not in visitedNodes and grid.isMovable(nextX, nextY):
                    childNode = Node(nextX, nextY, node, node.pathCost + 1)
                    unvisitedNodes.append(
                        (childNode, Path.getFullPathFromNode(node)))
                    changes.append(((nextX, nextY), 'frontier'))
            frontierStack.extend(unvisitedNodes[::-1])
        return None, countedNodes, changes


class BreadthFirstSearch(IUninformedSearch):
    def search(self, grid: Grid, start: tuple[int, int], goal: tuple[int, int]):
        frontierQueue = deque([[Node(start[0], start[1])]])
        countedNodes = 0
        visitedNodes = set()
        changes = []
        while frontierQueue:
            node = frontierQueue.popleft()[-1]
            countedNodes += 1
            if (node.x, node.y) == goal:
                return Path.getFullPathFromNode(node), countedNodes, changes
            visitedNodes.add((node.x, node.y))
            changes.append(((node.x, node.y), 'visited'))
            for directionX, directionY in Direction.getTupleValues():
                nextX, nextY = directionX + node.x, directionY + node.y
                if (nextX, nextY) not in visitedNodes and grid.isMovable(nextX, nextY):
                    childNode = Node(nextX, nextY, node, node.pathCost + 1)
                    frontierQueue.append(
                        Path.getFullPathFromNode(node) + [childNode])
                    visitedNodes.add((nextX, nextY))
                    changes.append(((nextX, nextY), 'frontier'))
        return None, countedNodes, changes


class CustomSearchOne(IUninformedSearch):

    def dls(self, grid: Grid, start: tuple[int, int], goal: tuple[int, int], limit: int):
        frontier = [(Node(start[0], start[1]), [], 0)]
        visited = set()
        counted_nodes = 0
        changes = []

        while frontier:
            node, path, depth = frontier.pop()
            counted_nodes += 1

            if (node.x, node.y) == goal:
                return Path.getFullPathFromNode(node), counted_nodes, changes

            if (node.x, node.y) not in visited:
                visited.add((node.x, node.y))
                changes.append(((node.x, node.y), 'visited'))

                if depth < limit:
                    for directionX, directionY in Direction.getTupleValues():
                        nextX, nextY = node.x + directionX, node.y + directionY
                        if (nextX, nextY) not in visited and grid.isMovable(nextX, nextY):
                            childNode = Node(
                                nextX, nextY, node, node.pathCost + 1)
                            frontier.append(
                                (childNode, path + [(node.x, node.y)], depth + 1))
                            changes.append(((nextX, nextY), 'frontier'))

        return None, counted_nodes, changes

    def iddfs(self, grid, start, goal):
        depth_limit = 0
        while True:
            result, counted_nodes, changes = self.dls(
                grid, start, goal, depth_limit)
            if result:
                return result, counted_nodes, changes
            depth_limit += 1

    def search(self, grid: Grid, start: tuple[int, int], goal: tuple[int, int]):
        result, counted_nodes, changes = self.iddfs(grid, start, goal)
        return result, counted_nodes, changes
