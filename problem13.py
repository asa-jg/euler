data = [[int(number) for number in row.split()]for row in open("problem13text.txt")]
su = 0
print(len(data))
for i in range(100):
    for x in data[i]:
        su = su + int(x)
print(su)
    
        
    