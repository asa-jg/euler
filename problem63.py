import time
start_time = time.time()

lst = []
for i in range(1,100):
    for k in range(1,100):
        lst.append([i**k, k])
res = []
for x in lst:
    if len(str(x[0])) == x[1]:
        res.append(x)
print(len(res))
print("--- %s seconds ---" % (time.time() - start_time))
