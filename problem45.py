import time
import math
start_time = time.time()

lst =[]
for i in range(1,10000000000):
    lst.append(i*(3*i-1)/2)

def is_pen(num):
    for i in range(math.floor(num/100)):
        if num == int(i*(3*i-1)/2):
            return True 
    return False

def is_hex(num):
    for i in range(math.floor(num/100)):
        if num == int(i*(2*i-1)):
            return True 
    return False
res = []
for x in lst:
    if is_hex(x) and is_pen(x) and x != 40755:
        print(x)
        print("--- %s seconds ---" % (time.time() - start_time))
        quit()
print("--- %s seconds ---" % (time.time() - start_time))




