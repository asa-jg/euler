lst =[]
lst2 = []
for b in range(10):
    for c in range(10):
        for x in range(900,999):
            if (100001*9 + 10010*b+1100*c)%x == 0 and (100001*9 + 10010*b+1100*c)/x <1000:
                    lst.append([b,c,x])
for x in lst:
    lst2.append(100001*9+10010*x[0]+1100*x[1])
    
print(max(lst2))