from Components import Parser
from Components import Grid
from Components import Searcher, Path

import sys


def main() -> None:
    inFile = sys.argv[1] if sys.argv[1] != "" else print(
        "Please provide a file name or UI to run the GUI.")
    if sys.argv[1] != "ui":
        a = Parser(fileName=inFile).parse()
        filename = a["fileName"]
        cols, rows = a["gridSize"]
        g = Grid(rows, cols)
        for wall in a['walls']:
            g.appendWall(*wall)

        s = Searcher(
            g, a['startLocation'], a['goalLocation'], sys.argv[2].upper())
        paths, totalNodes, c = s.getResult()
        print(f"{filename} {sys.argv[2]}")
        if (len(paths) > 1):
            for i in range(0, len(paths)):
                if paths[i] is not None:
                    print(
                        f"<Node ({a['goalLocation'][i][0]}, {a['goalLocation'][i][1]})> {totalNodes[i]}")
                    print([Path.reinterpretPath(paths[i][j], paths[i][j+1])
                           for j in range(0, len(paths[i]) - 1)])
                else:
                    print(
                        f"<Node ({a['goalLocation'][i][0]}, {a['goalLocation'][i][1]})> {totalNodes[i]}")
                    print(f"No goal is reachable; {totalNodes[i]}")

        else:
            if paths[0] is not None:
                print(
                    f"{paths[0][-1]} {totalNodes}")
                print([Path.reinterpretPath(paths[0][i], paths[0][i+1])
                       for i in range(0, len(paths[0]) - 1)])
            else:
                print(
                    f"<Node ({a['goalLocation'][0][0]}, {a['goalLocation'][0][1]})> {totalNodes[0]}")
                print(f"No goal is reachable; {totalNodes[0]}")
    else:
        from Components import MainUI
        MainUI().mainloop()


if __name__ == "__main__":
    main()
