def appearsonce(lst):
    lst2 = []
    lst3=[]
    for x in lst:
        if x not in lst2:
            if x not in lst3:
                lst2.append(x)
        else:
            lst2.remove(x)
            lst3.append(x)
              
    return lst2
lst = []
for a in range(2,101):
    for b in range(2,101):
        lst.append(a**b)
lst = set(lst)
print(len(appearsonce(lst)))