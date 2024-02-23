sum = 0
def convert(num):
    li = [int(x) for x in str(num)]
    return li
d1 = {0:0,1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
d2 = {2: 6, 3: 6, 4: 5, 5: 5, 6: 5, 7: 7, 8: 6, 9: 6}

for i in range(1,20):
    sum += d1[i]
    
for i in range(20,100):
    temp = convert(i)
    sum = sum + d2[temp[0]]+d1[temp[1]]
print(sum)
    
    