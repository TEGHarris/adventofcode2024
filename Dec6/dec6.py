with open("Dec6Input.txt") as f:
    area = f.readlines()
    area = [x.strip() for x in area]
for i in range(len(area)):
    area[i] = list(area[i])

def findLocation():
    global area
    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j] in ["^", "v", "<", ">"]:
                return i,j

def moveForward(row, col):
    global area
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

while True:
    Row, Col = findLocation()
    if area[Row][Col] == "^" and Row > 0 and area[Row-1][Col] == "#":
        rotate(Row, Col)
    elif area[Row][Col] == "v" and Row+1 < len(area) and area[Row+1][Col] == "#":
        rotate(Row, Col)
    elif area[Row][Col] == "<" and Col > 0 and area[Row][Col-1] == "#":
        rotate(Row, Col)
    elif area[Row][Col] == ">" and Col+1 < len(area[Row]) and area[Row][Col+1] == "#":
        rotate(Row, Col)
    try:
        Row, Col = moveForward(Row, Col)
    except IndexError:
        break

total = 0
for i in range(len(area)):
    for j in range(len(area[i])):
        if area[i][j] in ["X", "^", "v", "<", ">"]:
            total += 1
print(total)