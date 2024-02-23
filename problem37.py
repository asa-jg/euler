from euler import is_prime, primes
import math
import time
start_time = time.time()

lst = primes(1000000)
def trunc_ltr(num):
    trunc = [num]
    val = str(num)
    for i in range(len(val)-1):
        trunc.append(int(val[1:]))
        val = val[1:]
    return trunc

def trunc_rtl(num):
    trunc = [num]
    val = str(num)
    for i in range(1,len(val)):
        trunc.append(int(val[0:-i]))
    return trunc

def is_list_prime(List):
    for x in List:
        if not is_prime(x):
            return False
    return True
res = []
for x in lst:
    if is_list_prime(trunc_ltr(x)) and is_list_prime(trunc_rtl(x)):
        res.append(x)
res.remove(2)
res.remove(3)
res.remove(5)
res.remove(7)
print(sum(res),len(res))
print("--- %s seconds ---" % (time.time() - start_time))      
    