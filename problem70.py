import time
import math
from euler import totient, checkperm, primes
start_time = time.time()

minimum = 10000
val = 0
primeslist = primes(5000)
primeslist2 = primes(2000)
primeslist3 = [x for x in primeslist if x not in primeslist2]

list_of_mults = [x*y for x in primeslist3 for y in primeslist3 if x*y < 10000000]
print(len(list_of_mults))
for i in list_of_mults:
    if checkperm(str(i),str(totient(i))):
        if i/totient(i) < minimum:
            minimum = i/totient(i)
            val = i
print(val)        
print("--- %s seconds ---" % (time.time() - start_time))
