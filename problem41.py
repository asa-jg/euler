import time
import math
import itertools
from euler import is_prime
from euler import ltn
start_time = time.time()
lst = list(itertools.permutations([1,2,3,4,5,6,7]))

def ltn(List):
    string = ''
    for x in List:
        string+=str(x)
    return int(string)
res = []
for x in lst:
    if is_prime(ltn(x)):
        res.append(ltn(x))
print(max(res))
        
        
        
print("--- %s seconds ---" % (time.time() - start_time))  
