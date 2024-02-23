import time
start_time = time.time()
res = [1]
for i in range(100):
    res.append(0)
coins = list(range(1,100))
for x in coins:
    for i in range(x,101):
        res[i]=res[i]+res[i-x]
print(res[100])
    
print("--- %s seconds ---" % (time.time() - start_time))
