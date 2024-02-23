import time
start_time = time.time()
n=2
for i in range(1,7830457):
    n = 2*n%10000000000
n*=28433
n+=1
n%=10000000000
print(n)
print("--- %s seconds ---" % (time.time() - start_time))
