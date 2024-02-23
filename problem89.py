import time
start_time = time.time()

with open('text_romans.txt', 'r') as f:
    lst1 = [[num for num in line.split()] for line in f]
lst = []
for x in lst1:
    lst.append(x[0])
print(lst)
print("--- %s seconds ---" % (time.time() - start_time))
