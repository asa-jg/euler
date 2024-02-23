import time
start_time = time.time()
from euler import is_prime
tr = [1]; tl = [1]; br = [1]; bl = [1]
searching = True
i = 1
r = 0
lst =[]
primes = []
while searching:
    tr.append(tr[-1] + 8*i)
    tl.append(tl[-1]+8*i-2)
    br.append(br[-1]+8*i-6)
    bl.append(bl[-1]+8*i-4)
    lst = [tr[-1]] + [tl[-1]] + [br[-1]] + [bl[-1]]
    for x in lst:
        if is_prime(x):
            r+=1
            primes.append(x)
    ratio = r/(len(tr)*4-3)
    if ratio < 0.1:
        searching = False
    i+=1
print(len(tr)*2-1, primes)
        

print("--- %s seconds ---" % (time.time() - start_time))
