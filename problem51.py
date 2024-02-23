import time
import math
from euler import primes, is_prime, binarySearch
start_time = time.time()#

primelist = primes(1000000)
strings = []

def genstrings(s, index):
    if index > 0:
        strings.append(s)
    for x in range(index, len(s)):
        genstrings(createplaceholder(s, x), x+1)
        
        

def createplaceholder(s, index):
    return s[0:index] + '*' + s[index+1:]

for x in primelist:
    strings = []
    genstrings(str(x),0)
    for y in range(1, len(strings)):
        count = 0
        for z in range(10):
            check = strings[y].replace('*',str(z))
            check = int(check)
            if len(str(check)) < len(strings[y]):
                continue
            if binarySearch(check,primelist) >= 0:
                count +=1
            if count == 8:
                print(check)
    



print("--- %s seconds ---" % (time.time() - start_time))