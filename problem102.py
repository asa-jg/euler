import time
import math
start_time = time.time()
a_file = open("text_102.txt", "r")

data = []
for line in a_file:
    stripped_line = line.strip()
    line_list = stripped_line.split(',')
    data.append(line_list)
a_file.close()

coords = []
for x in data:
    coords.append([int(x[0]),int(x[1]),int(x[2]),int(x[3]),int(x[4]),int(x[5])])
print(coords)

def area(lst):
    return abs((0.5)*(lst[0]*(lst[3]-lst[5])+lst[2]*(lst[5]-lst[1])+lst[4]*(lst[1]-lst[3])))

epsilon = 0.005
def area_origin(lst):
    area_1 = abs((0.5)*(0*(lst[3]-lst[5])+lst[2]*(lst[5]-0)+lst[4]*(0-lst[3])))
    area_2 = abs((0.5)*(lst[0]*(0-lst[5])+0*(lst[5]-lst[1])+lst[4]*(lst[1]-0)))
    area_3 = abs((0.5)*(lst[0]*(lst[3]-0)+lst[2]*(0-lst[1])+0*(lst[1]-lst[3])))
    return area_1 + area_2 + area_3
val = 0
for x in coords:
    if int(area_origin(x)-area(x)) == 0:
        val+=1
print(val)

print("--- %s seconds ---" % (time.time() - start_time))
