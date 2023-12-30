import sys

if (len(sys.argv) != 3):
    print("Pass the input and output files as arguments", file=sys.stderr)
    exit()

inputFilePath = sys.argv[1]
outputFilePath = sys.argv[2]

try:
    with open(inputFilePath, 'r') as inputFile, open(outputFilePath, 'w') as outputFile:
        for line in inputFile:
            changedLine = f'"{line.strip()}",\n'
            outputFile.write(changedLine)
except FileNotFoundError:
    print(f"The file '{inputFilePath}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
