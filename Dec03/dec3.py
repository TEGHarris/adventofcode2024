import re
myregex = r"mul\(\d+,\d+\)"


with open("Dec3input.txt","r") as f:
    fileAsString = f.read()

# for i in range(len(fileAsString)):
#     if not [i] == "m" and [i+1] == "u" and [i+2] == "l":
#         continue
#     else:
#         print(fileAsString[i:i+5])

matches = re.findall(myregex,fileAsString)
total = 0
for i in range(len(matches)):
    matches[i] = matches[i].replace("mul(","")
    matches[i] = matches[i].replace(")","")
    matches[i] = matches[i].split(",")
    matches[i] = int(matches[i][0]) * int(matches[i][1])
    total += matches[i]
print(total)