with open("Dec9Input.txt") as f:
    data = f.read()
    data = data.strip()



def expandList(data):
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
    return expandedList

def checkList(expandedList,start,length):
    for i in range(start,start+length):
        if i >= len(expandedList):
            return False
        if expandedList[i] != ".":
            return False
    return True


usedWorkingValue = []
expandedList = expandList(data)
for i in range(len(expandedList)-1,-1,-1): # iterate backwards through the list
    if expandedList[i] == ".":
        continue
    else:
        if expandedList[i] not in usedWorkingValue:
            workingValue = expandedList[i]
            usedWorkingValue.append(workingValue)
        else:
            continue
        length = 0
        while True:
            if expandedList[i-length] != expandedList[i]:
                break
            length += 1
        placeToGo = False # and since you've no place to go, let it snow, let it snow, let it snow
        for j in range(len(expandedList)):
            if j >= i:
                break
            if checkList(expandedList,j,length):
                for k in range(j,j+length):
                    expandedList[k] = workingValue # set the values to working value
                placeToGo = True
                break
        if placeToGo:
            for l in range(length):
                expandedList[i-l] = "." # set the values to free space
        print(expandedList)
    print(i)


print("Finished modifying the list")
total = 0
for k in range(len(expandedList)):
    if expandedList[k] == ".":
        continue
    total += (int(expandedList[k])*k)
print (f"total is {total}")