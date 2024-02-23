import time
import math
start_time = time.time()
res = []
for i in range(100000):
    counter = 1
    searching = True
    val = ''
    while searching:
        if len(val + str(i*counter)) > 9:
            searching = False
        else:
            val = val + str(i*counter)
            counter +=1
    if len(set(val)) == 9 and '0' not in set(val):
        res.append(val)
print(max(res))
        

print("--- %s seconds ---" % (time.time() - start_time))      
