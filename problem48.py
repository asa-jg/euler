import time
from euler import primes
start_time = time.time()
val = 0
for i in range(1,1001):
    val +=i**i
print(val)
print("--- %s seconds ---" % (time.time() - start_time))

    
