# Filename: CreateTestCases.py
# Author: Xuan Tuan Minh Nguyen
# Date: 2024-05-21
# Description: Create Horn Form and Generic Propositional Form test cases

from os import listdir
import random
import string


class TestGenerator:
    def __init__(self):
        self.symbols = []
        self.clauses = []

    def generateHornCase(self, parent_folder):
        # get the current number of test cases
        current_number_of_test = len(
            [file for file in listdir(parent_folder) if "test" in file])
        for i in range(50):
            # create a list of symbols
            self.symbols = list(string.ascii_letters[:5])
            clauses = []
            for j in range(12):
                # ge th random number of symbols in a clause
                hornClause = list(
                    set(random.choices(self.symbols, k=random.randint(1, 5))))
                tail = hornClause[:-1]
                # if the clause has more than 2 symbols, add operation and add it to the list of clauses
                if len(hornClause) >= 2:
                    head = hornClause[-1]
                    clauseString = "&".join(tail) + " =>" + head
                    clauses.append(clauseString)
            literal = list(
                set(random.choices(self.symbols, k=random.randint(1, 3))))
            clauses.extend(literal)
            # create query
            query = random.choice(self.symbols)

            while query in literal:
                query = random.choice(self.symbols)
            # write to file
            with open(parent_folder+"test" + str(current_number_of_test + i)+".txt", "w") as file:
                file.write("TELL\n")
                for clause in clauses:
                    file.write(clause)
                    file.write("; ")
                file.write("\n")
                file.write("ASK\n")
                file.write(query)

    def generateGeneralCase(self,  parent_folder, number, maxdepth=4):
        # get the current number of test cases
        current_number_of_test = len(
            [file for file in listdir(parent_folder) if "test" in file])
        for j in range(number):
            # write to file
            with open(parent_folder+"test" + str(current_number_of_test + j)+".txt", "w") as file:
                file.write("TELL\n")
            self.clauses = []
            # create a list of symbols
            self.symbols = {symbol: 1 for symbol in list(
                string.ascii_lowercase[:7])}
            symbol = random.choice(list(self.symbols.keys()))
            clause = ""
            for i in range(0, 6):
                # create a clause
                clause = "("
                # generate 2 random symbols for the left clause
                firstSymbol = random.choice(list(self.symbols.keys()))
                secondSymbol = random.choice(list(self.symbols.keys()))
                # ensure that the depth of the clause is less than maxdepth and the 2 symbols are different
                while self.symbols[firstSymbol] + self.symbols[secondSymbol] > maxdepth or firstSymbol == secondSymbol:
                    firstSymbol = random.choice(list(self.symbols.keys()))
                    secondSymbol = random.choice(list(self.symbols.keys()))
                depth = self.symbols[firstSymbol] + self.symbols[secondSymbol]

                # generate negation operator
                if (random.randint(0, 1) == 0):
                    firstSymbol = "~"+firstSymbol

                if (random.randint(0, 1) == 0):
                    secondSymbol = "~"+secondSymbol
                clause += firstSymbol
                operator = random.randint(0, 3)
                # generate operator
                if operator == 0:
                    clause += "&"
                elif operator == 1:
                    clause += "||"
                elif operator == 2:
                    clause += "=>"
                elif operator == 3:
                    clause += "<=>"
                clause += secondSymbol
                clause += ")"
                # update the depth of the clause in the list
                self.symbols.update({clause: depth})
                if i != 5:
                    with open(parent_folder+"test" + str(current_number_of_test + j)+".txt", "a") as file:
                        file.write(clause)
                        file.write(";")
            with open(parent_folder+"test" + str(current_number_of_test + j)+".txt", "a") as file:
                file.write("\n")
                file.write("ASK\n")
                file.write(clause)


TestGenerator().generateHornCase("./Components/Datasets/HornTestCases/")
TestGenerator().generateGeneralCase("./Components/Datasets/GeneralTestCases/", 50)
