with open("Dec4Input.txt", "r") as f:
    data = f.readlines()

wordsearch = []
for line in data:
    wordsearch.append(list(line.strip()))

# print (wordsearch)
total = 0

def checkX(row,col):
    check = False
    if row == 0 or row == len(wordsearch)-1 or col == 0 or col == len(wordsearch[0])-1:
        return False
    if ((wordsearch[row-1][col-1] == "M" and wordsearch[row+1][col+1] == "S") or (wordsearch[row-1][col-1] == "S" and wordsearch[row+1][col+1] == "M")) and ((wordsearch[row-1][col+1] == "M" and wordsearch[row+1][col-1] == "S") or (wordsearch[row-1][col+1] == "S" and wordsearch[row+1][col-1] == "M")):
        check = True
    return check
for row in range(len(wordsearch)):
    for column in range(len(wordsearch[0])):
        if wordsearch[row][column] == "A":
            if checkX(row,column):
                total += 1
        else:
            continue
print(total)