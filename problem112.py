import time
import sys
start_time = time.time()

def is_increasing(n):
    n = str(n)
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

def is_decreasing(n):
    n = str(n)
    for i in range(len(n)-1):
        if n[i] < n[i+1]:
            return False
    return True

val = 0
up_to = 1587000
for i in range(1,up_to+1):
    if not is_decreasing(i) and not is_increasing(i):
        val +=1

print("percentage is ", (val/up_to)*100, "% with n =", up_to)

                    
            
        
        
    

print("--- %s seconds ---" % (time.time() - start_time))
