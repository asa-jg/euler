counter = []
res = 0
for i in range(2,10000000):
    res = 0
    for x in str(i):
        if res+int(x)**5 <= i:
            res += int(x)**5
        else:
            res = 10**10
    if res == i:
        counter.append(res)
print(sum(counter))
            