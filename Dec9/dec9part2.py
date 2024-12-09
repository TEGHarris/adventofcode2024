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

for i in range(len(expandedList)-1,-1,-1):
    if expandedList[i] == ".":
        continue
    else:
        workingValue = expandedList[i]
        length = 1
        while True:
            if expandedList[i-length] == expandedList[i]:
                expandedList[i] = "."
                length += 1
            else:
                break
        
        for j in range(len(expandedList)):
            for i in range(length):
                if expandedList[j+i] != '.':
                    flag = False
            if expandedList[j] == '.':
                expandedList[j] = str(workingValue)
                break

total = 0
for k in range(len(expandedList)):
    if expandedList[k] == ".":
        break
    total += (int(expandedList[k])*k)
print (total)