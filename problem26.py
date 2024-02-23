lst = []
for i in range(1,1001):
    lst.append(1/i)

print(lst)
mx = 1
lst2 = []
for x in lst:
    if len(str(x)) >= mx:
        mx = len(str(x))
        lst2.append(x)
lst2.remove(1.0)
lst2.remove(0.5)
print(lst2)

def recl(num):
    searching = True
    i = 1
    first = 0
    string = str(num)
    while searching:
        if string[i] != 0:
            t = string[i]
            searching = False
            first = i
            
        i +=1

    searching = True
    while searching:
        if string[i] == t:
            return i - first
        i+=1
length =1
for x in lst2:
    if recl(x) >= length:
        vl = x
        length = recl(x)
print(len(str(0.01)))
        
    
    
        