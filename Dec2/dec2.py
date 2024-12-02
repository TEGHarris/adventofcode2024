f = open("Dec2Input.txt", "r")
lines = f.readlines()
#this is a test line
valid = 0
steadyIncrease = False
steadyDecrease = False

def checkNumberPair(a,b,steadyIncrease,steadyDecrease,i):
    # global steadyIncrease
    # global steadyDecrease
    if abs(b -a) > 3 or abs(b - a) < 1:
        return False
    if i == 1:
        if b > a:
            steadyIncrease = True
        if b < a:
            steadyDecrease = True
    else:
        if b > a and steadyDecrease:
            return False
        if b < a and steadyIncrease:
            return False
    return True

for line in lines:
    steadyIncrease = False
    steadyDecrease = False
    workingReport = line.split()
    for i in range(len(workingReport)):
        if i == 0:
            continue
        if not checkNumberPair(int(workingReport[i-1]),int(workingReport[i]),steadyIncrease,steadyDecrease,i):
            break
        if i == len(workingReport) - 1:
            valid += 1
