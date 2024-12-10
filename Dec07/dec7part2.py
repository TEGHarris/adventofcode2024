import numpy as np
with open("Dec7Input.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]

targets = []
options = []

for line in data:
    x = line.split(": ")
    targets.append(x[0])
    options.append(x[1].split(" "))

total = 0 # this is the value to output
def concatenate(a, b):
    return int(str(a) + str(b))

for i in range(len(targets)):
    for j in range(3**(len(options[i])-1)):
        asBinary = str((np.base_repr(j,base = 3)).zfill(len(options[i])-1)) # interpret the 0s as + and 1s as * and the 2s are ||
        count = int(options[i][0])
        for k in range(len(asBinary)):
            if asBinary[k] == "1":
                count *= int(options[i][k+1])
            elif asBinary[k] == "0":
                count += int(options[i][k+1])
            elif asBinary[k] == "2":
                count = concatenate(count, int(options[i][k+1]))
            else:
                print(f"ERROR: unexpected value. Binary is {asBinary[k]} of type {type(asBinary[k])}")
        print(f"DEBUG: target is {targets[i]} and options are {options[i]}. I am currently at {asBinary} and count is {count}.")
        if count == int(targets[i]):
            total += int(targets[i])
            break
print(total)