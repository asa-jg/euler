import time
from euler import is_pal
start_time = time.time()
 
lst = list(range(1,10001))
res = []

def radd(num):
    val = str(num)
    return num+int(val[::-1])




for x in lst:
    val = x
    counter = 0
    for i in range(50):
        if not is_pal(radd(x)):
            counter+=1
            if counter == 50:
                res.append(val)
        
        x = radd(x)


    

        
print(len(res),res)
print("--- %s seconds ---" % (time.time() - start_time))
