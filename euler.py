import math
from math import gcd
import collections

from functools import reduce

#generates all factors of n

def factors_all(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
#generates list of primes up to n

def primes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while(p * p <= n):  
        if (prime[p] == True):    
            for i in range(p * p, n + 1, p): 
                prime[i] = False
        p += 1
    c = []
    for p in range(2, n): 
        if prime[p]: 
            c.append(p)
    return c 

#checks if number is prime

def is_prime(n): 
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True

#converts list to string

def ltn(List):
    string = ''
    for x in List:
        string+=str(x)
    return int(string)

#converts number to binary

def ctb(num):
    binary = ''
    for i in range(21):
        j = 20-i
        if num < 2**(j):
            binary+=('0')
        if num >= 2**(j):
            binary+=('1')
            num = num - 2**(j)
    return int(binary)

#returns a list of the prime factors of a number

def factors(n): 
    lst = []  
    while n % 2 == 0: 
        lst.append(2) 
        n = n / 2
          
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        while n % i== 0: 
            lst.append(i) 
            n = n / i 
              
    if n > 2: 
        lst.append(n)
    return lst

#factorial

def fac(n):
    val = 1
    for i in range(1,n+1):
        val = val*i
    return val

#choose function

def choose(n,r):
    return (fac(n)/(fac(r)*fac(n-r)))

#checks if nummber is palindrome

def is_pal(num):
    val = str(num)
    for i in range(len(val)):
        if val[i] != val[-(1+i)]:
            return False
    return True

#totient function

def totient(n):
    amount = 0        
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount

def totatives(n):
    phi = int(n > 1 and n)
    for p in range(2, int(n ** .5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    #if n is > 1 it means it is prime
    if n > 1: phi -= phi // n 
    return phi

#binary search for increasing list#

def binarySearch(index, lst):
    start = 0
    end = len(lst)
    middle = int((end + start)/2)
    
    while(start < end 
          and lst[middle] != index 
          and middle < len(lst)):
        if lst[middle] < index:
            start = middle+1
        else:
            end = middle-1
        middle = int((end + start)/2)
    
    if middle < len(lst) and lst[middle] == index:
        return middle
    else:
        return -1

#checks if list or string is permutation 
def checkperm(a, b):
    d = collections.defaultdict(int)
    for x in a:
        d[x] += 1
    for x in b:
        d[x] -= 1
    return not any(d.values())



#read a file and make a list of the entries
#file = open("names.txt")
#data = [line.split('","') for line in file]
#res = data[0]
