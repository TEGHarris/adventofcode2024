#opening the file and transfering the data to a list
table = []
with open("Dec1Input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = ((line.strip()).split("   "))
        table.append(line)



def bubbleSort(arr):
    n = len(arr)
    hasSwapped = True
    while hasSwapped:
        hasSwapped = False
        for i in range(n - 1):
            if arr[i][0] > arr[i + 1][0]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                hasSwapped = True
    return arr

#this splits the numbers into two lists.
# Note to get the number as an integer, you need bignumbers[i][0] not bignumbers[i]
bigNumbers = []
smallNumbers = []

for i in range(len(table)):
    small = [int(num) for num in table[i][0].split()]
    big = [int(num) for num in table[i][1].split()]
    smallNumbers.append(small)
    bigNumbers.append(big)

smallNumbers = bubbleSort(smallNumbers)
bigNumbers = bubbleSort(bigNumbers)
#finds the distance between the two points
totaldistance = 0
for i in range(len(smallNumbers)):
    totaldistance += abs(smallNumbers[i][0] - bigNumbers[i][0])
print(totaldistance)