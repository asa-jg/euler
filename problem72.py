import time start_time = time.time()
from euler import totient

val = 0

for x in range(1,1000001):
    val = val+totient(x)
print(val)








print("--- %s seconds ---" % (time.time() - start_time))
