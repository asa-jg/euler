import time
import math
start_time = time.time()
const = ''
for i in range(500000):
    const += str(i)
res = []
print(const)
for k in range(7):
    res.append(const[10**(k)])
print(5*3*7*2)
    


print("--- %s seconds ---" % (time.time() - start_time))  