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
for i in range(75):
    new_data = []
    for stone in data:
        if stone == 0:
            new_data.append(1)
        elif len(str(stone)) % 2 == 0:
            midpoint = len(str(stone)) // 2
            new_data.append(int(str(stone)[:midpoint]))
            new_data.append(int(str(stone)[midpoint:]))
        else:
            new_data.append(stone * 2024)
    data = np.array(new_data)
    print(f"Completed {i+1} of 75")
    #print(f"After {i+1} blink(s): {data}")
print(f"Final length of data: {len(data)}")