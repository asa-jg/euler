res = [1]
for i in range(200):
    res.append(0)
coins = [1,2,5,10,20,50,100,200]
for x in coins:
    for i in range(x,201):
        res[i]=res[i]+res[i-x]
print(res[200])
    