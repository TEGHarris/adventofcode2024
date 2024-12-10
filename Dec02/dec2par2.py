f = open("Dec2Input.txt", "r")
lines = f.readlines()
valid = 0
steadyIncrease = False
steadyDecrease = False

def checkNumberPair(a, b, i):
    global steadyIncrease, steadyDecrease
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


def isSafe(workingReport):
    for i in range(len(workingReport)):
        if i == 0:
            continue
        if not checkNumberPair(int(workingReport[i-1]), int(workingReport[i]), i):
            break
        if i == len(workingReport) - 1:
            return True


for line in lines:
    steadyIncrease = False
    steadyDecrease = False
    workingReport = line.split()
    print("-------------------- ")
    print (f"now working on :{workingReport}")
    if isSafe(workingReport):
        valid += 1
        print("This report is safe")
    else:
        print("This report is not safe")
        for i in range(len(workingReport)):
            steadyIncrease = False
            steadyDecrease = False
            workingReportCopy = workingReport.copy()
            workingReportCopy.pop(i)
            if isSafe(workingReportCopy):
                valid += 1
                print("This report is safe after removing element at index", i)
                break
print(valid)