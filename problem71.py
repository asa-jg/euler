import time
import random
from math import gcd
start_time = time.time()

num = 428571
denom = 1000000
lst = []

for j in range(10):
    for k in range(10):
            if gcd(num+k, denom+j) == 1 and (num+k)/(denom+j) < 3/7:
                lst.append([num+k,denom+j,(num+k)/(denom+j)])
            if gcd(num-k, denom+j) == 1 and (num-k)/(denom+j) < 3/7:
                lst.append([num-k,denom+j,(num-k)/(denom+j)])
            if gcd(num+k, denom-j) == 1 and (num+k)/(denom-j) < 3/7:
                lst.append([num+k,denom-j,(num+k)/(denom-j)])
            if gcd(num-k, denom-j) == 1 and (num-k)/(denom-j) < 3/7:
                lst.append([num-k,denom-j,(num-k)/(denom-j)])
                
lst.sort(key=lambda x: x[2])
res = []
for x in lst:
    res.append(x[2])
res.sort()
print(res[-1])
print(lst[-1])
#read the question 
print("--- %s seconds ---" % (time.time() - start_time))
