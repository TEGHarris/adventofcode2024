import copy
with open("Dec6Input.txt") as f:
    area = f.readlines()
    area = [x.strip() for x in area]
for i in range(len(area)):
    area[i] = list(area[i])

def findLocation(area):
    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j] in ["^", "v", "<", ">"]:
                return i,j

def moveForward(row, col, area):
    if area[row][col] == "^" and row > 0:
        area[row][col] = "X"
        area[row-1][col] = "^"
        return row-1, col
    elif area[row][col] == "v" and row < len(area) - 1:
        area[row][col] = "X"
        area[row+1][col] = "v"
        return row+1, col
    elif area[row][col] == "<" and col > 0:
        area[row][col] = "X"
        area[row][col-1] = "<"
        return row, col-1
    elif area[row][col] == ">" and col < len(area[row]) - 1:
        area[row][col] = "X"
        area[row][col+1] = ">"
        return row, col+1
    else:
        raise IndexError

def rotate(row,col):
    global area
    if area[row][col] == "^":
        area[row][col] = ">"
    elif area[row][col] == "v":
        area[row][col] = "<"
    elif area[row][col] == "<":
        area[row][col] = "^"
    elif area[row][col] == ">":
        area[row][col] = "v"

originalRow, originalCol = findLocation(area)
total = 0
for row in range(len(area)):
    for col in range(len(area[row])):
        areaClone = copy.deepcopy(area)
        if areaClone[row][col] ==".":
            areaClone[row][col] = "#"
        else:
            continue # no point placing boxes where there are already boxes
        count = 0 # represents the number of times the guard passes through it start position
    while True:
        Row, Col = findLocation(areaClone)
        if areaClone[Row][Col] == "^" and Row > 0 and areaClone[Row-1][Col] == "#":
            rotate(Row, Col)
        elif areaClone[Row][Col] == "v" and Row+1 < len(areaClone) and areaClone[Row+1][Col] == "#":
            rotate(Row, Col)
        elif areaClone[Row][Col] == "<" and Col > 0 and areaClone[Row][Col-1] == "#":
            rotate(Row, Col)
        elif areaClone[Row][Col] == ">" and Col+1 < len(areaClone[Row]) and areaClone[Row][Col+1] == "#":
            rotate(Row, Col)
        
        try:
            Row, Col = moveForward(Row, Col, areaClone)
        except IndexError:
            break
        
        if Row == originalRow and Col == originalCol:
            count += 1
            if count == 2:
                total += 1
                break 
print(total)



