import time
from euler import primes, factors, is_prime
start_time = time.time()

p_lst = primes(100000000)

def divprime(num):
    for y in factors(num):
        if not is_prime(y+y/num):
            return False
    return True

print(divprime(30))
res = []
for x in p_lst:
    if divprime(x+1):
        res.append(x+1)
print(sum(res))
    

print("--- %s seconds ---" % (time.time() - start_time))

    
        