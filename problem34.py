def fac(num):
    val = 1
    for i in range(1,num+1):
        val = val*i
    return val
res = []
for i in range(100000):
    counter = 0
    for x in str(i):
        x = int(x)
        counter +=fac(x)
    if counter == i:
        res.append(i)
print(sum(res))
        