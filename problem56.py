import time
start_time = time.time()

biggest = 0
for i in range(1,100):
    for j in range(1,100):
        val = str(i**j)
        counter = 0
        for k in val:
            counter+= int(k)
        if counter > biggest:
            biggest = counter
            
print(biggest)
print("--- %s seconds ---" % (time.time() - start_time))
