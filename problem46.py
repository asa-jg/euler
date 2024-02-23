import time
import math
from euler import primes, is_prime
start_time = time.time()

lst = primes(300)
lst.remove(2)
lst2 = []
for x in lst:
    for y in lst:
        lst2.append(x*y)
        

for x in lst2:
    counter = 0
    for k in range(math.floor(x**(1/2))+1):
        if not is_prime(x - 2*k**2):
            counter = counter+1
            if counter == math.floor(x**(1/2))+1:
                print(x)
                print("--- %s seconds ---" % (time.time() - start_time))
                quit()
print("--- %s seconds ---" % (time.time() - start_time))

    
        
