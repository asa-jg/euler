def stl(string):
    res = []
    for x in str(string):
        res.append(x)
    return res
        

e = 0.000000001
lst = []
for i in range(10,100):
    for j in range(10,100):
        li = stl(i)
        lj = stl(j)
        if i != j and i%10 != 0:
            for x in li:
                if x in lj:
                    li.remove(x)
                    lj.remove(x)
                    if int(li[0]) != 0 and int(lj[0]) != 0:
                        if abs(int(li[0])/int(lj[0]) - i/j) < e:
                            lst.append([i,j])
        
print(lst)

print((16/64)*(19/95)*(26/65)*(49/98))
                    
                    