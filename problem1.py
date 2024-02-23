def multiples(n):
    lst = []
    for i in range(n+1):
        if i%3 ==0 or i%5 == 0:
            lst.append(i)
    return lst

print(sum(multiples(1000)))
            