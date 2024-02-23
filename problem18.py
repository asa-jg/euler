lst = []
lst2 = []
for i in range(len(lst)):
    for k in range(len(lst[i])):
        lst[i][k]
summ = [59]
reading = []
print(lst2)
for i in range(1,len(lst)):
    for k in range(len(lst[i])):
        if k == 0:
            reading.append(summ[0]+lst[i][k])
        if k == len(lst[i])-1:
            reading.append(summ[k-1]+lst[i][k])
        if k != 0 and k < len(lst[i]) and k != len(lst[i])-1:
            reading.append(max(summ[k-1],summ[k])+lst[i][k])

    summ = reading
    reading = []
print(max(summ))
    