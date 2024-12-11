with open("Dec11Input.txt") as f:
    data = f.read().strip().split(" ")
    data = [int(x) for x in data]


def shiftAll(data,stop):
    data.append(".")
    for i in range(len(data)-1, stop, -1):
        if i == stop:
            break
        if i == stop +1:
            data[i] = -1
        else:
            data[i] = data[i-1] 
        


for i in range(25):
    for stone in range(len(data)):
        if data[stone] == 0:
            data[stone] = 1
        elif len(str(data[stone])) % 2 != 0:
            data[stone] = data[stone] * 2024
        else:
            shiftAll(data, stone)
            midpoint = len(str(data[stone])) / 2
            data[stone+1] = str(data[stone])[midpoint:]