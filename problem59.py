import time
from collections import Counter
start_time = time.time()

def most_frequent(List): 
    occurence_count = Counter(List) 
    return occurence_count.most_common(1)[0][0]

file = open("text_cipher.txt")
data = [line.split(',') for line in file]
res = []
for x in data[0]:
    res.append(int(x))
first =[]
second = []
third = []
for i in range(int(len(res)/3)):
    first.append(res[3*i])
    second.append(res[3*i+1])
    third.append(res[3*i+2])
key = []
key.append(chr(most_frequent(first)^ord(' ')))
key.append(chr(most_frequent(second)^ord(' ')))
key.append(chr(most_frequent(third)^ord(' ')))
print(key)

sol = []

for i in range(len(first)):
    sol.append(chr(first[i]^ord(key[0])))
    sol.append(chr(second[i]^ord(key[1])))
    sol.append(chr(third[i]^ord(key[2])))
counter = ''
for x in sol:
    counter+=x
print(counter)


print("--- %s seconds ---" % (time.time() - start_time))


