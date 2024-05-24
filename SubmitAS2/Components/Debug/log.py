def logResultToFile(result, filename):
    with open(filename, 'w') as file:
        file.write(result)
        file.close()
