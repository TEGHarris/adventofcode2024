with open("rules.txt") as f:
    rules = f.readlines()
    rules = [x.strip() for x in rules] # opening the rules file and storing the rules in a list

with open("manuals.txt") as f:
    manuals = f.readlines()
    manuals = [x.strip() for x in manuals] # opening the manuals file and storing the manuals in a list

for i in range(len(manuals)):
    manuals[i] = manuals[i].split(",") # splitting the manuals into a 2d array
for i in range(len(rules)):
    rules[i] = rules[i].split("|") # splitting the rules into a 2d array

def NeededRules(manual):
    newlist = rules.copy()
    for i in range(len(rules) - 1, -1, -1):
        if rules[i][0] not in manual or rules[i][1] not in manual:
            newlist.pop(i)
    return newlist
# FROM HERE ABOVE IS THE SAME AS THE ORIGINAL CODE

def checkIfInvalid(manual, needed): # THE ISSUE IS HERE
    flag = True #Flag is true on a valid manual
    for j in range(len(needed)):
        if manual.index(needed[j][0]) > manual.index(needed[j][1]):
            flag = False
            break
    if not flag:
        return True
    return False
        

def rearrange(manual):
    workingManual = manual.copy()
    needed = NeededRules(workingManual)
    while True:
        for i in range(len(needed)):
            if workingManual.index(needed[i][0]) > workingManual.index(needed[i][1]):
                temp = workingManual.index(needed[i][0])
                index1 = workingManual.index(needed[i][0])
                index2 = workingManual.index(needed[i][1])
                temp = workingManual[index1]
                workingManual[index1] = workingManual[index2]
                workingManual[index2] = temp
        if not checkIfInvalid(workingManual, needed):
            break
    return workingManual

invalid_manuals = []

for i in range(len(manuals)):
    needed = NeededRules(manuals[i]) # needed is a list of rules that are needed for the manual
    if checkIfInvalid(manuals[i], needed):
        invalid_manuals.append(manuals[i]) # finding the invalid manuals
        continue
for i in range(len(invalid_manuals)):
    invalid_manuals[i] = rearrange(invalid_manuals[i])



finalTotal = 0
for i in range(len(invalid_manuals)):
    middleValue = int(invalid_manuals[i][len(invalid_manuals[i]) // 2])
    finalTotal += middleValue
print(finalTotal)