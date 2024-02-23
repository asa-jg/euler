a = [1,2,3,4,5,6,7,8,9]
res = []
for i in range(1000):
    for j in range(1000):
        counter = []
        q = str(i)
        w = str(j)
        e = str(i*j)
        for p in q:
            counter.append(int(p))
        for p in w:
            counter.append(int(p))
        for p in e:
            counter.append(int(p))
        counter.sort()
        if counter == a:
            res.append(i*j)
res = set(res)
print(res)
print(sum(res))