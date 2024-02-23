import time
import math
#
start_time = time.time()
lowest = 2000000
for n in range(1000):
    for m in range(1000):
        numrecs = int((n+1)*n*m*(m+1)/4)
        distance = abs(2000000 - numrecs)
        if distance < lowest:
            lowest = distance
            area = n*m
print(area, lowest)

        


print("--- %s seconds ---" % (time.time() - start_time))
