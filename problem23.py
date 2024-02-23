import math
import time
def sum_divisors(num):
    div_lst = []
    for i in range(1,math.floor(num/2)+1):
        if num%i == 0:
            div_lst.append(i)
    return sum(div_lst)
abn = []
for i in range (1,28124):
   if sum_divisors(i) >i:
       abn.append(i)
       

a = []
b = [i for i in range(1,28124)]

for i in range(len(abn)):
    for j in range(i,len(abn)):
        if abn[i]+abn[j]<28124:
            a.append(abn[i]+abn[j])
a = set(a)

                
print(sum(b)-sum(a))
print(time.process_time())               
    