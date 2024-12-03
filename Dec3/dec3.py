import re
myregex = "mul\(\d+,\d+\)"


with open("Dec3input.txt","r") as f:
    fileAsString = f.read()

# for i in range(len(fileAsString)):
#     if not [i] == "m" and [i+1] == "u" and [i+2] == "l":
#         continue
#     else:
#         print(fileAsString[i:i+5])

matches = re.findall(myregex,fileAsString)

for i in range(len(matches)):
    print(matches[i])