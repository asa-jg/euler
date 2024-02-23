import time
import math
start_time = time.time()

lst = [i * i for i in range(10000)]

def s_num_check(n):
    n_sqrt = int(math.sqrt(n))
    n_string = str(n)
    length = len(n_string)
    if length % 2 == 0:
        block_size = int(length/2)
        
    
    

for x in lst:
    




print("--- %s seconds ---" % (time.time() - start_time))