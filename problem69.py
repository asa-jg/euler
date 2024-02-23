import time
start_time = time.time()
from euler import totatives, fac, primes, check


lst = primes(10000)
val = 1
for x in lst:
    if val*x < 1000000:
        val = val * x
    
print(val)

print("--- %s seconds ---" % (time.time() - start_time))
