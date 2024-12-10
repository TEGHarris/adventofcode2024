with open("Dec10Input.txt") as f:
    data = f.read()
    data = data.split("\n")
    data = [list(i)for i in data]


def findingNines(data,start,x,y):


for i in range(len(data)):
    for j in range(len(data[i])):
        if int(data[i][j]) > 0:
            continue
        else:
            pass

findingNines(data,7,0,0)