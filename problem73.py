import time
from math import gcd

start_time = time.time()

def totient(n):
    amount = 0
    lst = []
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
            lst.append(k)
    return lst
fracs = 0
def gen_fracs(n,lst):
    x = 0
    for i in(lst):
        if i/n < 1/2 and i/n > 1/3:
            x+=1
    return x

for i in range(1,12001):
    fracs = fracs + gen_fracs(i,totient(i))

print(fracs)
print("--- %s seconds ---" % (time.time() - start_time))
