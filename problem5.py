factorial = 2432902008176640000
def recursion(n):
    i = 2
    res = n
    counter = 0
    while i<=20:
        print (res)
        if res%i == 0:
            res = res/i
            counter = 1
        else:
            if counter == 1:
                res = res*i
                counter = 0
            i = i+1
    return res

print(recursion(factorial))