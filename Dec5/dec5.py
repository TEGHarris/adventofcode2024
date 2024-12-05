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

valid_manuals = []
for i in range(len(manuals)):
    needed = NeededRules(manuals[i]) # needed is a list of rules that are needed for the manual
