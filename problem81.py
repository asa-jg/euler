import time
start_time = time.time()
with open('text_matrix.txt', 'r') as f:
    lst = [[int(num) for num in line.split(',')] for line in f]
#lst = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]    
summ = [4445]
reading = []
for i in range(1,len(lst)):
    for k in range(i+1):
        if k == 0:
            reading.append(summ[k]+lst[i][k])
        if k == i:
            reading.append(summ[k-1]+lst[i-k][k])
        if k != i and k != 0 and k < len(lst[i]):
            reading.append(min(summ[k-1], summ[k])+lst[i-k][k])
        
    summ = reading
    reading = []
for i in range(len(lst)-1):
    for k in range(1,len(lst)-i):
        reading.append(min(summ[k-1], summ[k])+lst[len(lst)-k][i+k])
    summ = reading
    reading = []

print(summ)
print(min(summ))
    

print("--- %s seconds ---" % (time.time() - start_time))