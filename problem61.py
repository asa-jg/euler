import time
import math
start_time = time.time()

triangles = []
squares = []
pents = []
hexs = []
hepts = []
octs = []
for n in range(45,141):
    triangles.append([int(n*(n+1)/2),0])
    
for n in range(32,100):
    squares.append([int(n**2),1])

for n in range(26,82):
    pents.append([int(n*(3*n-1)/2),2])
    
for n in range(23,71):
    hexs.append([int(n*(2*n-1)),3])

for n in range(21,64):
    hepts.append([int(n*(5*n-3)/2),4])

for n in range(19,59):
    octs.append([int(n*(3*n-2)),5])

full_list = triangles+squares+pents+hexs+hepts+octs

cycle = []
types = []
def check(x,y):
    if str(x[0])[-2] == str(y[0])[0] and str(x[0])[-1] == str(y[0])[1] and y[1] not in types:
        return True
    else:
        return False
        
for x in full_list:
    cycle = []
    types = []
    types.append(x[1])
    cycle.append(x[0])
    for y in full_list:
        if check(x,y):
            cycle.append(y[0])
            types.append(y[1])
            for z in full_list:
                if check(y,z):
                    types.append(z[1])
                    cycle.append(z[0])
                    for a in full_list:
                        if check(z,a):
                            types.append(a[1])
                            cycle.append(a[0])
                            for b in full_list:
                                if check(a,b):
                                    types.append(b[1])
                                    cycle.append(b[0])
                                    for c in full_list:
                                        if check(b,c) and str(x[0])[0]==str(c[0])[-2] and str(x[0])[1] == str(c[0])[-1]:
                                            cycle.append(c[0])
                                            types.append(c[1])
                                            print(sum(cycle))
                                    types.pop()
                                    cycle.pop()
                            types.pop()
                            cycle.pop()
                    types.pop()
                    cycle.pop()
            types.pop()
            cycle.pop()
            

print("--- %s seconds ---" % (time.time() - start_time))
