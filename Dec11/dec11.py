with open("example.txt") as f:
    content = f.read().strip()
    data = content.split(" ")
    data = [int(x) for x in data]


# def shiftAll(data,stop):
#     data.append(-1)
#     for i in range(len(data)-1, stop, -1):
#         if i == stop:
#             break
#         data[i] = data[i-1] 
        

previousWasSplit = False
for i in range(6):
    for stone in range(len(data)):
        if previousWasSplit:
            previousWasSplit = False
            continue
        if data[stone] == 0:
            data[stone] = 1
        elif len(str(data[stone])) % 2 == 0:
            previousWasSplit = True
            midpoint = len(str(data[stone])) // 2
            data.insert(stone+1, int(str(data[stone])[midpoint:]))
            data[stone] = int(str(data[stone])[:midpoint])
        else:
            data[stone] = data[stone] * 2024

    print(f"After {i+1} blink(s): {data}")
print(f"Final length of data: {len(data)}")