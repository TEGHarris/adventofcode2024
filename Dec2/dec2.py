f = open("Dec2Input.txt", "r")
lines = f.readlines()

valid = 0

def checkNumberPair(a,b,steadyIncrease,steadyDecrease,isFirstPair):
    if abs(b -a) > 3 or abs(b - a) < 1:
        return False
    if isFirstPair:
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
    isFirstPair = True
    for i in range(len(workingReport)):
        if i == 0:
            continue
        if not checkNumberPair(int(workingReport[i-1]),int(workingReport[i]),steadyIncrease,steadyDecrease,isFirstPair):
            break
        if i == len(workingReport) - 1:
            valid += 1
        isFirstPair = False
