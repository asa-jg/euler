import time
from primes import ctb
start_time = time.time()
pal = []



def is_pal(num):
    val = str(num)
    for i in range(len(val)):
        if val[i] != val[-(1+i)]:
            return False
    return True
    

for i in range(1,10):
    pal.append(i)
for i in range(1,10):
    pal.append(i*10+i)
for i in range(1,10):
    for j in range(10):
        pal.append(i*100+i+j*10)
for i in range(1,10):
    for j in range(10):
        pal.append(i*1000+i+j*100+j*10)
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            pal.append(i*10000+i+j*1000+j*10+k*100)
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            pal.append(i*100000+i+j*10000+j*10+k*100+k*1000)
            
res = []
for x in pal:
    if is_pal(ctb(x)):
        res.append(x)
print(sum(res))
        
              
print("--- %s seconds ---" % (time.time() - start_time))
        