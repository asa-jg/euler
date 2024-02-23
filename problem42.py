import time
start_time = time.time()

file = open("text_words.txt")
data = [line.split('","') for line in file]
data = data[0]
data[0] = 'A'
data[-1] = 'YOUTH'
tri = [0.0, 1.0, 3.0, 6.0, 10.0, 15.0, 21.0, 28.0, 36.0, 45.0, 55.0, 66.0, 78.0, 91.0, 105.0, 120.0, 136.0, 153.0, 171.0, 190.0, 210.0, 231.0, 253.0, 276.0, 300.0, 325.0, 351.0]
res = 0
for x in data:
    current = 0
    for i in range(len(x)):
        current+=(ord(x[i])-64)
    if current in tri:
        res+=1
print(res)
        
    
    
    
print("--- %s seconds ---" % (time.time() - start_time))  
