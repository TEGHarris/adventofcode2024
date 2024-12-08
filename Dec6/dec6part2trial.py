import copy
with open("example.txt") as f:
    area = f.readlines()
    area = [x.strip() for x in area]
for i in range(len(area)):
    area[i] = list(area[i])

def findLocation(area):
    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j] in ["^", "v", "<", ">"]:
                return i, j

def moveForward(row, col):
    if areaClone[row][col] == "^" and row > 0:
        areaClone[row][col] = "X"
        areaClone[row-1][col] = "^"
        return row-1, col
    elif areaClone[row][col] == "v" and row < len(areaClone) - 1:
        areaClone[row][col] = "X"
        areaClone[row+1][col] = "v"
        return row+1, col
    elif areaClone[row][col] == "<" and col > 0:
        areaClone[row][col] = "X"
        areaClone[row][col-1] = "<"
        return row, col-1
    elif areaClone[row][col] == ">" and col < len(areaClone[row]) - 1:
        areaClone[row][col] = "X"
        areaClone[row][col+1] = ">"
        return row, col+1
    else:
        raise IndexError

def rotate(row,col):
    if areaClone[row][col] == "^":
        areaClone[row][col] = ">"
    elif areaClone[row][col] == "v":
        areaClone[row][col] = "<"
    elif areaClone[row][col] == "<":
        areaClone[row][col] = "^"
    elif areaClone[row][col] == ">":
        areaClone[row][col] = "v"

originalRow, originalCol = findLocation(area)
total = 0
visited_locations = set()

for row in range(len(area)):
    for col in range(len(area[row])):
        if area[row][col] == ".":
            areaClone = copy.deepcopy(area)
            areaClone[row][col] = "#"
        else:
            continue # no point placing boxes where there are already boxes
        count = 0 # represents the number of times the guard passes through its start position
        visited_locations.clear() # reset visited locations for each new box placement
        Row, Col = findLocation(areaClone) 
        while True:
            if areaClone[Row][Col] == "^" and Row > 0 and areaClone[Row-1][Col] == "#":
                rotate(Row, Col)
            elif areaClone[Row][Col] == "v" and Row+1 < len(areaClone) and areaClone[Row+1][Col] == "#":
                rotate(Row, Col)
            elif areaClone[Row][Col] == "<" and Col > 0 and areaClone[Row][Col-1] == "#":
                rotate(Row, Col)
            elif areaClone[Row][Col] == ">" and Col+1 < len(areaClone[Row]) and areaClone[Row][Col+1] == "#":
                rotate(Row, Col)
            
            try:
                Row, Col = moveForward(Row, Col)
            except IndexError:
                break
            
            if (Row, Col) == (originalRow, originalCol):
                count += 1
            else:
                visited_locations.add((Row, Col))
            if count == 2:
                total += 1
                break 
print(total)



