with open("Dec4Input.txt", "r") as f:
    data = f.readlines()

wordsearch = []
for line in data:
    wordsearch.append(list(line.strip()))

# print (wordsearch)
total = 0
def checkUp(row,col):
    if row < 3:
        return False
    if wordsearch[row-1][col] == "M" and wordsearch[row-2][col] == "A" and wordsearch[row-3][col] == "S":
        return True
    return False


def checkDown(row,col):
    if row > len(wordsearch)-4:
        return False
    if wordsearch[row+1][col] == "M" and wordsearch[row+2][col] == "A" and wordsearch[row+3][col] == "S":
        return True
    return False

def checkLeft(row,col):
    if col < 3:
        return False
    if wordsearch[row][col-1] == "M" and wordsearch[row][col-2] == "A" and wordsearch[row][col-3] == "S":
        return True
    return False

def checkRight(row,col):
    if col > (len(wordsearch[0])-4):
        return False
    if wordsearch[row][col+1] == "M" and wordsearch[row][col+2] == "A" and wordsearch[row][col+3] == "S":
        return True
    return False

def checkUpRight(row,col):
    if row < 3 or col > len(wordsearch[0])-4:
        return False
    if wordsearch[row-1][col+1] == "M" and wordsearch[row-2][col+2] == "A" and wordsearch[row-3][col+3] == "S":
        return True
    return False

def checkUpLeft(row,col):
    if row < 3 or col < 3:
        return False
    if wordsearch[row-1][col-1] == "M" and wordsearch[row-2][col-2] == "A" and wordsearch[row-3][col-3] == "S":
        return True
    return False

def checkDownRight(row,col):
    if row > len(wordsearch)-4 or col > len(wordsearch[0])-4:
        return False
    if wordsearch[row+1][col+1] == "M" and wordsearch[row+2][col+2] == "A" and wordsearch[row+3][col+3] == "S":
        return True
    return False

def checkDownLeft(row,col):
    if row > len(wordsearch)-4 or col < 3:
        return False
    if wordsearch[row+1][col-1] == "M" and wordsearch[row+2][col-2] == "A" and wordsearch[row+3][col-3] == "S":
        return True
    return False

def checkAll(row,col):
    n = 0
    if checkUp(row,col):
        n += 1
    if checkDown(row,col):
        n += 1
    if checkLeft(row,col):
        n += 1
    if checkRight(row,col):
        n += 1
    if checkUpRight(row,col):
        n += 1
    if checkUpLeft(row,col):
        n += 1
    if checkDownRight(row,col):
        n += 1
    if checkDownLeft(row,col):
        n += 1
    return n

for row in range(len(wordsearch)):
    for column in range(len(wordsearch[0])):
        if wordsearch[row][column] == "X":
            total += checkAll(row,column)
        else:
            continue
print(total)