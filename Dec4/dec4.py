with open("Dec4Input.txt") as f:
    data = f.readlines()

wordsearch = []
for line in data:
    wordsearch.append(list(line))

print (wordsearch)

def checkUp(row,col):
    if row == 0:
        return False
    if wordsearch[row-1][col] == "M" and wordsearch[row-2][col] == "A" and wordsearch[row-3][col] == "S":
        return True
    return False


def checkDown(row,col):
    if row == len(wordsearch)-1:
        return False
    if wordsearch[row+1][col] == "M" and wordsearch[row+2][col] == "A" and wordsearch[row+3][col] == "S":
        return True
    return False

def checkLeft(row,col):
    if col == 0:
        return False
    if wordsearch[row][col-1] == "M" and wordsearch[row][col-2] == "A" and wordsearch[row][col-3] == "S":
        return True
    return False

def checkRight(row,col):
    if col == len(wordsearch[0])-1:
        return False
    if wordsearch[row][col+1] == "M" and wordsearch[row][col+2] == "A" and wordsearch[row][col+3] == "S":
        return True
    return False

def checkUpRight(row,col):
    if row == 0 or col == len(wordsearch[0])-1:
        return False
    if wordsearch[row-1][col+1] == "M" and wordsearch[row-2][col+2] == "A" and wordsearch[row-3][col+3] == "S":
        return True
    return False

def checkUpLeft(row,col):
    if row == 0 or col == 0:
        return False
    if wordsearch[row-1][col-1] == "M" and wordsearch[row-2][col-2] == "A" and wordsearch[row-3][col-3] == "S":
        return True
    return False