def fac(a):
    val = 1
    for i in range(1,a+1):
        val = val*i
    return val
a = 0
    
lst = []
numbers = [0,1,2,3,4,5,6,7,8]
for i in range(1,10):
    searching = True
    counter  = 0
    j = 10 - i
    print(a)
    for x in numbers:
        while searching:
            if x ==2:
                a = a+2*fac(j)
                searching = False
                numbers.remove(2)
                lst.append(2)
            if a + x*fac(j) >= 1000000 and x != 2:
                a = a+(x-1)*fac(j)
                searching = False
                numbers.remove(x)
                lst.append(x)
            break
print(lst)