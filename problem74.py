import time
import math
from euler import fac
start_time = time.time()

def fod(n):
    n = str(n)
    val = 0
    for x in n:
        val = val+fac(int(x))
    return val
print(fod(145))

def len_loop(n):
    searching = True
    lst = [n]
    val = n
    while searching:
        if val == 169:
            return len(lst)+2
            print("yes")
        if val == 363601:
            return len(lst)+1
        if val == 1454:
            return len(lst)
        if val == 871:
            return len(lst)+1
        if val == 45361:
            return len(lst)
        if val == 45362:
            return len(lst)
        val = fod(val)
        lst.append((val))
        if lst.count((val)) == 2:
            searching = False
            return len(lst)-1
result = 0        
for i in range(1000000):
    if len_loop(i) == 60:
        result +=1
print(result)

print("--- %s seconds ---" % (time.time() - start_time))
