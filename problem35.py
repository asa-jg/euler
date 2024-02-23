import time
import math
start_time = time.time()

def primes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while(p * p <= n):  
        if (prime[p] == True):    
            for i in range(p * p, n + 1, p): 
                prime[i] = False
        p += 1
    c = []
    for p in range(2, n): 
        if prime[p]: 
            c.append(p)
    return c 
lst = primes(1000000)
res = []

def is_prime(n): 
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True

def c(num):
    c = []
    val = str(num)
    for i in range(len(val)):
        c.append(int(val[1:] + val[0]))
        val = val[1:] + val[0]
    return c

def pl(st):
    counter = 0
    for i in st:
        if not is_prime(i):
            return False
    return True
tup = 0
for x in lst:
    if pl(c(x)):
        tup+=1
        res.append(x)
    
        
print(res,tup)      
print("--- %s seconds ---" % (time.time() - start_time))      

        
    
    

