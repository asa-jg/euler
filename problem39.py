import time
import math
start_time = time.time()
biggest = 0
for i in range(1,1000):
    current = []
    for j in range(1,math.floor(i/2)+1):
        for k in range(1,math.floor(i/2)+1):
            if j**2 + k**2 == (i-j-k)**2:
                current.append([i,j,k,i-j-k])
    if len(current) > biggest:
        res = i
        biggest = len(current)
print(res)
        
    

print("--- %s seconds ---" % (time.time() - start_time))      
