with open("example.txt") as f:
    data = f.read()
    data = data.split("\n")
    data = [list(i)for i in data]


def checkPath(data,zy,zx,ny,nx):
    currentX = zx
    currentY = zy
    count = int(data[zy][zx]) + 1
    while currentX != nx and currentY != ny and len(data[i]) >currentX > -1 and len(data) > currentY > -1: # while not in correct position
        possibleDirections = []
        if int(data[currentY-1][currentX]) == count:
            possibleDirections.append("u")
        if int(data[currentY+1][currentX]) == count:
            possibleDirections.append("d")
        if int(data[currentY][currentX-1]) == count:
            possibleDirections.append("l")
        if int(data[currentY][currentX+1]) == count:
            possibleDirections.append("r")

        
        if len(possibleDirections) == 0:
            return False
        else:
            for i in range(len(possibleDirections)):
                if possibleDirections[i] == "u":
                    if checkPath(data,currentY-1,currentX,ny,nx):
                        currentY -= 1
                        count += 1
                        break
                elif possibleDirections[i] == "d":
                    if checkPath(data,currentY+1,currentX,ny,nx):
                        currentY += 1
                        count += 1
                        break
                elif possibleDirections[i] == "l":
                    if checkPath(data,currentY,currentX-1,ny,nx):
                        currentX -= 1
                        count += 1
                        break
                elif possibleDirections[i] == "r":
                    if checkPath(data,currentY,currentX+1,ny,nx):
                        currentX += 1
                        count += 1
                        break
    return True
    


total =0
for i in range(len(data)):
    for j in range(len(data[i])):
        if int(data[i][j]) > 0:
            continue
        else:
            for k in range(len(data)):
                for l in range(len(data[k])):
                    if int(data[k][l]) == 9:
                        if checkPath(data,i,j,k,l):
                            total += 1
print(total)