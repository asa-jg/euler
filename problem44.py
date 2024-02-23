import time
start_time = time.time()
lst = []
for i in range(1,10000):
    lst.append(i*(3*i-1)/2)
print(lst)
for x in lst:
    for y in lst:
        if (x+y) in lst and (x-y) in lst:
            print(x-y)
            quit()
            print("--- %s seconds ---" % (time.time() - start_time))
print("--- %s seconds ---" % (time.time() - start_time))

    