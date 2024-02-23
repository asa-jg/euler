import time
import math
import itertools
from euler import is_prime, ltn
start_time = time.time()
lst = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))

def ltn(List):
    string = ''
    for x in List:
        string+=str(x)
    return int(string)
lst2 = []
for x in lst:
    lst2.append(ltn(x))

def ssd(num):
    val = str(num)
    if (int(val[1:4]))%2 !=0:
        return False
    if (int(val[2:5]))%3 !=0:
        return False
    if (int(val[3:6]))%5 !=0:
        return False
    if (int(val[4:7]))%7 !=0:
        return False
    if (int(val[5:8]))%11 !=0:
        return False
    if (int(val[6:9]))%13 !=0:
        return False
    if (int(val[7:10]))%17 !=0:
        return False
    return True
res = []

for i in range(len(lst2)):
    if ssd(lst2[i]):
        res.append(lst2[i])

print(sum(res))


print("--- %s seconds ---" % (time.time() - start_time))  
