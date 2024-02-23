import time
start_time = time.time()

coords = []
for x1 in range(51):
    for y1 in range(51):
        for x2 in range(51):
            for y2 in range(51):
                coords.append([x1,y1,x2,y2])
print(len(coords))
print("--- %s seconds ---" % (time.time() - start_time))
