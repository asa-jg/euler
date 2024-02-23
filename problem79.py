import time
start_time = time.time()
file = open("text_keylog.txt")
data = [line.split('\n') for line in file]
data2 = []
for x in data:
    data2.append(int(x[0]))

#lol did it by hand
print(data2)
print("--- %s seconds ---" % (time.time() - start_time))
