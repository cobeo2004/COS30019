from Components.Interfaces.IReadFile import IReader
from Components.Decorator.Export import export


@export
class ReadFile(IReader):
    def readAll(self, fn: str):
        # Initialize empty lists to hold lines, flattened content, tell statements, and the query
        lines = []
        flattened = []

        tell, query = [], []

        # Open the file and read each line
        with open(fn) as f:
            for line in f:
                # Strip whitespace, convert to lowercase, split by semicolon, and add to lines
                lines.append(line.strip().lower().split(";"))

        # Flatten the list of lists into a single list of values
        for subList in lines:
            for value in subList:
                flattened.append(value)

        # Try to find the index of the "ask" keyword in the flattened list
        try:
            queryIndex = flattened.index("ask")
        except ValueError:
            # If "ask" is not found, set queryIndex to the length of the flattened list
            queryIndex = len(flattened)

        # Process values before the "ask" keyword as tell statements
        for value in flattened[:queryIndex]:
            if value not in ["", "tell", "ask"]:
                # Remove spaces from the value and add it to the tell list
                tell.append(value.replace(" ", ""))

        # If there's a query after "ask", process it
        if queryIndex + 1 < len(flattened):
            query = flattened[queryIndex + 1].replace(" ", "")
        else:
            query = ""

        # Return the tell statements and the query
        return tell, query
