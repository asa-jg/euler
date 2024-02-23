dictionary = {}
dictionary[1] = 1

def collatz(num):
    collatz_seq = [num]
    temp = num
    while temp not in dictionary:
        if temp%2 == 0:
            temp = temp/2
            collatz_seq.append(temp)
        else:
            temp = 3*temp+1
            collatz_seq.append(temp)
    for i in range(len(collatz_seq)):
        dictionary[collatz_seq[i]] = dictionary[temp] +len(collatz_seq) - i
    return dictionary[num]
        
    
            
biggest = 1
num = 1
for i in range(1,1000001):
    if collatz(i)>biggest:
        biggest = collatz(i)
        num = i
        
print(num)
    
    
    