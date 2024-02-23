import time
start_time = time.time()
num = [1,3]
denom = [1,2]
for i in range(999):
    num.append(num[-1]*2+num[-2])
    
for i in range(1,1001):
    denom.append(denom[-1]+num[i])
print(denom)
counter = 0
for i in range(len(num)):
    if len(str(num[i]))> len(str(denom[i])):
        counter+=1
print(counter)

print("--- %s seconds ---" % (time.time() - start_time))
