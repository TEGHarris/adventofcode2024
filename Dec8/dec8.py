import sys

with open("Dec8Input.txt") as f:
    antennas = [list(x.strip()) for x in f]

antiNodes = [["."] * len(antennas[0]) for i in range(len(antennas))]




def findAntiNode(primaryRow, primaryCol, secondaryRow, secondaryCol):
    rise = primaryRow - secondaryRow
    run = 1 *(primaryCol - secondaryCol)
    x = primaryCol + run
    y = primaryRow + rise
    if x < 0 or y < 0 or x >= len(antennas[0]) or y >= len(antennas):
        print(f"AntiNode is out of bounds but it would be at position ({y}, {x}) and of type {antennas[primaryRow][primaryCol]}. The origin points are ({primaryRow}, {primaryCol}) and ({secondaryRow}, {secondaryCol})")
        return
    elif antiNodes[y][x] == ".":
        antiNodes[y][x] = "#"
        print(f"Found antiNode at position ({y}, {x}) of type {antennas[primaryRow][primaryCol]}")
        return
    else:
        print(f"AntiNode already exists at position ({y}, {x})")
        return

def countAntiNodes():
    count = 0
    for i in range(len(antiNodes)):
        for j in range(len(antiNodes[0])):
            if antiNodes[i][j] == "#":
                count += 1
    print(f"Total number of antiNodes: {count}")
    sys.exit()


def findAntenna():
    for i in range(len(antennas)):
        for j in range(len(antennas[0])):
            if antennas[i][j] != ".":
                workingAntennaType = antennas[i][j]
                return workingAntennaType
            if i == len(antennas) - 1 and j == len(antennas[0]) - 1:
                print("All antennas are used")
                return None

while True:
    # Go through the antennas and see for new one
    workingAntennaType = findAntenna()
    if workingAntennaType is None:
        countAntiNodes()
        break

    for i in range(len(antennas)):
        for j in range(len(antennas[0])):
            if antennas[i][j] == workingAntennaType:
                # Check for all other antennas
                for k in range(len(antennas)):
                    for l in range(len(antennas[0])):
                        if antennas[k][l] == workingAntennaType:
                            if (i != k) and (j != l):
                                findAntiNode(i, j, k, l)
                                                    
                    # at the end, turn all used antennas to "."
    for i in range(len(antennas)):
        for j in range(len(antennas[0])):
            if antennas[i][j] == workingAntennaType:
                antennas[i][j] = "."

# the answer must be greater than 318
# not 374