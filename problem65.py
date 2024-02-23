import time
import math
start_time = time.time()
from fractions import Fraction

e = []
def gen_to(lst,n):
    k = 1
    for i in range(1,n):
        if (i+1)%3 == 0:
            lst.append(2*k)
            k+=1
        else:
            lst.append(1)
    return lst

def get_frac(lst):
    frac = [1,int((lst[-2]*lst[-1]+1)/lst[-1])]
    for i in range(3,len(lst)+2):
        k = len(lst) - i 
        frac2 = [frac[1],lst[k]*frac[1]+frac[0]]
        frac = frac2
        print(frac)
    print([frac[0]+frac[1],frac[0]])
    return [frac[0]+frac[1],frac[0]]
        


def dec_numerator(lst):
    val = str(lst[0])
    summ = 0
    for x in val:
        summ = summ + int(x)
    return summ
        
x = gen_to(e,100)
print(x)
print(dec_numerator(get_frac(x)))
print("--- %s seconds ---" % (time.time() - start_time))
