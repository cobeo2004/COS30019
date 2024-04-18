# Assignment 1 - Tree Based Search

## Description

In the field of Artificial Intelligence, using tree-based search algorithms for solving the Robot Navigation problem has been one of the most significant attentions in the context of pathfinding solutions. Throughout the years, multiple algorithms and solutions has been proposed to the public for solving the problem of Robot Navigation. The proposed solutions could be divided into two types of searching algorithms: Uninformed Search and Informed Search.

## Requirements

This report is written to provide a comparison between the two given algorithmic approaches, which give an overview on the algorithms, the complexity, and the performance of each algorithm on a sample map. Furthermore, this report hands out the implementation of each algorithm on Python code, some encountered features and bugs and short research of visualizing the pathfinding algorithms using Tkinter library and the implemented algorithms.

## Installation and Usage

In order to output the moving steps from the start point to the goal point, simply navigate to the Command Line Interface, change the directory to “\Build\main”, and use the following syntax as provided in Figure 1: “main <filename> <method>” (or “python main.py <filename> <method>”), where <filename> is the text file contains the grid size (m x n), agent’s initial coordinates, goal coordinates seperated by a “|” character, and the coordinates of the walls. And the <method> is the searching algorithm, it could be entered in both uppercase and lowercase and must follows the following list: dfs, bfs, gbfs, as, cus1, cus2. Besides, the program also have the ability to visualize the pathfinding algorithm using tkinter and the six implemented algorithm. Simply heads back to Command Line Interface (in the same directory of “\Build\main”, and type in the syntax that is provided in Figure 2: “main UI” (or “python main.py ui”). Figure 3 illustrates the first interface of the program, which let the user customizing the size of the grid (rows, columns and cell size) and choose which algorithm to executes. Figure 4 on the other hand is the main interface of the program, where user can chooses the starting and ending state of the agent and customizes the amount of walls (self-created or random-generated). During searching, the nodes in the frontier (not visited yet) are shown in the dark pink while the expanded nodes will be displayed in light pink. After the search is finished, the path will be illustrated with a green color.

## License

MIT License
