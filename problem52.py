import time
from euler import primes, is_prime
start_time = time.time()

for i in range(1,1666666):
    current = set(str(i))
    if set(str(i)) == set(str(2*i)) == set(str(3*i)) == set(str(4*i)) == set(str(5*i)) == set(str(6*i)):
        print(i)
    
        print("--- %s seconds ---" % (time.time() - start_time))
        quit()
