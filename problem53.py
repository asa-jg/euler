import time
start_time = time.time()

def fac(n):
    val = 1
    for i in range(1,n+1):
        val = val*i
    return val

def choose(n,r):
    if n >= r:
        return (fac(n)/(fac(r)*fac(n-r)))
    return



lst = list(range(1, 101))
data = []
for i in range(len(lst)):
    for j in range(i,len(lst)):
        data.append(choose(lst[j],lst[i]))
print(data)
res = []     
print(res)
for x in data:
    if not x is None:
        if x > 1000000:
            res.append(x)
print(len(res))


print("--- %s seconds ---" % (time.time() - start_time))
