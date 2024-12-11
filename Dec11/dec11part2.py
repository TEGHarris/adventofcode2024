import numpy as np


with open("Dec11Input.txt") as f:
    content = f.read().strip()
    data = content.split(" ")
    data = [int(x) for x in data]
    data = np.array(data)


# def shiftAll(data,stop):
#     data.append(-1)
#     for i in range(len(data)-1, stop, -1):
#         if i == stop:
#             break
#         data[i] = data[i-1] 
        

previousWasSplit = False
for i in range(25):
    stone = 0
    while True:
        if stone >= len(data):
            break
        if data[stone] == 0:
            data[stone] = 1
            stone += 1
            continue
        elif len(str(data[stone])) % 2 == 0:
            midpoint = len(str(data[stone])) // 2
            np.insert(data, stone+1, int(str(data[stone])[midpoint:]))
            data[stone] = int(str(data[stone])[:midpoint])
            stone += 2
        else:
            data[stone] = data[stone] * 2024
            stone +=1

    #print(f"After {i+1} blink(s): {data}")
print(f"Final length of data: {len(data)}")