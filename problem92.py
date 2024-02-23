import time
start_time = time.time()

d = {}

List = list(range(1,10000001))
counter = 0
def c(num):
    val = str(num)
    vole = 0
    for x in val:
        vole+=int(x)**2
    return vole

def chain(num):
    lst = []
    searching = True
    val = num
    if num in d:
        if d[num] == 89:
            return 1
        if d[num] == 1:
            return 0
    while searching:
        val = c(val)
        lst.append(val)
        if val == 1:
            for x in lst:
                d[x] = 1
            return 0
        if val == 89:
            for x in lst:
                d[x] = 89
            return 1

for i in List:
    counter+= chain(i)
    
print(counter)        
print("--- %s seconds ---" % (time.time() - start_time))
