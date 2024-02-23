import time
from euler import primes, is_prime
start_time = time.time()

lst = primes(1000000)
val = 0
for i in range(546):
    val+=lst[i]
for k in range(546):
    if is_prime(val-lst[k]):
        print(val-lst[k])
    val -= lst[k]
        
print("--- %s seconds ---" % (time.time() - start_time))
