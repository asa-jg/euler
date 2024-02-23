import time
import math
start_time = time.time()




limit=1500000
c=0
m=2
trips = []
while(c<limit):
    for n in range(1,m+1):
        a=m*m-n*n
        b=2*m*n
        c=m*m+n*n
        if(c>limit):
            break
        if(a==0 or b==0 or c==0):
            break
        trips.append([a,b,c])
    m=m+1
print(trips)

for x in trips:
    for y in trips:
        if sum(x) == sum(y):
            trips.remove(y)
print(len(trips))
            
print("--- %s seconds ---" % (time.time() - start_time))
