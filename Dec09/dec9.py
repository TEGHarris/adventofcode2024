with open("example.txt") as f:
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
print("Finished expanding the list")

for i in range(len(expandedList)-1,-1,-1):
    if expandedList[i] == ".":
        continue
    else:
        workingValue = expandedList[i]
        expandedList[i] = "."
        for j in range(len(expandedList)):
            if expandedList[j] == '.':
                expandedList[j] = str(workingValue)
                break
    print(i)
print("Starting to calculate the total")
total = 0
for k in range(len(expandedList)):
    if expandedList[k] == ".":
        break
    total += (int(expandedList[k])*k)
print (f"Answer is{total}")