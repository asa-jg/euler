file = open("names.txt")
data = [line.split('","') for line in file]
res = data[0]
res[0] = "MARY"
res[-1]="ALONSO"
res.sort()
val = 0
for i in range(len(res)):
    temp = 0
    for j in res[i]:
        temp = temp+(ord(j)-64)
    temp = temp*(i+1)
    val +=temp
    
print(val)

print(ord("A"))

        
        
    