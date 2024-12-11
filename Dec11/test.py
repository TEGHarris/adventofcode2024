data = [1,2,3,4,5,6,7,8,9,10]



def shiftAll(data,stop):
    data.append(".")
    for i in range(len(data)-1, stop, -1):
        if i == stop:
            break
        if i == stop +1:
            data[i] = -1
        else:
            data[i] = data[i-1] 

shiftAll(data,5)
print(data)