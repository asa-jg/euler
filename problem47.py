import time
import math
from euler import is_prime
start_time = time.time()

def factors(n): 
    lst = []  
    while n % 2 == 0: 
        lst.append(2), 
        n = n / 2
          
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        while n % i== 0: 
            lst.append(i), 
            n = n / i 
              
    if n > 2: 
        lst.append(n)
    return lst

def is_list_prime(List):
    for x in List:
        if not is_prime(x):
            return False
    return True

i = 644
searching = True

while searching:
    if is_list_prime(factors(i)) and len(set(factors(i))) == 4:
        if is_list_prime(factors(i+1)) and len(set(factors(i+1))) == 4:
            if is_list_prime(factors(i+2)) and len(set(factors(i+2))) == 4:
                if is_list_prime(factors(i+3)) and len(set(factors(i+3))) == 4:
                    searching = False
                else:
                    i+=4
            else:
                i+=3
        else:
            i+=2
    else:
        i+=1
            
        

print(i)
print("--- %s seconds ---" % (time.time() - start_time))
