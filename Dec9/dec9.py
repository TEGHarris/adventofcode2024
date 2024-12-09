with open("Dec9Input.txt") as f:
    data = f.read()
    data = data.strip()

expandedList = []
isData = True # a flag that switches between true for data and false for free space
id = 0
for i in range(len(data)):
    if isData:
        for j in range(int(data[i])):
            expandedList.append(str(id))
        isData = False
        id += 1
    else:
        for k in range(int(data[i])):
            expandedList.append(".")
        isData = True
for i in range
print(expandedList)