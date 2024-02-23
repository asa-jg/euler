import math
def sum_divisors(num):
    div_lst = []
    for i in range(1,math.floor(num/2)+1):
        if num%i == 0:
            div_lst.append(i)
    return sum(div_lst)
val = 0
for i in range(10000):
    if i == sum_divisors(sum_divisors(i)) and i != sum_divisors(i):
        val+=i

print(val)
    
    