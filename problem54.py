import time
start_time = time.time()
file = open("text_poker.txt")
data = [line.split(' ') for line in file]
for x in data:
    x[9] = x[9][:2]

player_1 = []
player_2 = []
for x in data:
    player_1.append([x[0],x[1],x[2],x[3],x[4]])
    player_2.append([x[5],x[6],x[7],x[8],x[9]])

def high_card(lst):
    values = []
    for x in lst:
        if x[0] == 'A':
            values.append(14)
        else:
            if x[0] == 'K':
                values.append(13)
            else:
                if x[0] == 'Q':
                    values.append(12)
                else:
                    if x[0] == 'J':
                        values.append(11)
                    else:
                        if x[0] == 'T':
                            values.append(10)
                        else:
                            values.append(int(x[0]))
            
    return max(values)

def high_card_straight(lst):
    values = []
    for x in lst:
        if x[0] == 'A':
            values.append(1)
            for y in lst:
                if y[0] == 'K':
                    if 1 in values:
                        values.remove(1)
                        values.append(14)
        else:
            if x[0] == 'K':
                values.append(13)
            else:
                if x[0] == 'Q':
                    values.append(12)
                else:
                    if x[0] == 'J':
                        values.append(11)
                    else:
                        if x[0] == 'T':
                            values.append(10)
                        else:
                            values.append(int(x[0]))
            
    values.sort()
    return values[-1]


def low_card(lst):
    values = []
    for x in lst:
        if x[0] == 'A':
            values.append(1)
            for y in lst:
                if y[0] == 'K':
                    if 1 in values:
                        values.remove(1)
                        values.append(14)
        else:
            if x[0] == 'K':
                values.append(13)
            else:
                if x[0] == 'Q':
                    values.append(12)
                else:
                    if x[0] == 'J':
                        values.append(11)
                    else:
                        if x[0] == 'T':
                            values.append(10)
                        else:
                            values.append(int(x[0]))
            
    values.sort()
    return values[0]

def pair(lst):
    for x in lst:
        for y in lst:
            if x!=y and x[0] == y[0]:
                return [True,x[0]]
    return [False,0]

def two_pair(lst):
    for x in lst:
        for y in lst:
            for z in lst:
                for a in lst:
                    if x!=y and x[0] == y[0] and x[0] != a[0] and a!=z and a[0] == z[0]:
                        return [True,x,a]
                    
    return [False]

def three_ok(lst):
    for x in lst:
        for y in lst:
            for z in lst:
                if x!=y and x!=z and z!=y and x[0] == y[0] == z[0]:
                    return [True,x]
    return [False]

def straight(lst):
    if high_card_straight(lst) - low_card(lst) == 4:
        if not pair(lst):
            return [True,high_card_straight(lst)]
    return [False]

def flush(lst):
    if lst[0][-1] == lst[1][-1] == lst[2][-1] == lst[3][-1] == lst[4][-1]:
        return [True,high_card(lst)]
    return [False]

def full_house(lst):
    for x in lst:
        for y in lst:
            for z in lst:
                for a in lst:
                    for b in lst:
                        if x!=y and x[0] == y[0] and x[0] != a[0] and a!=z and a!= b and b!=z and b[0] == a[0] == z[0]:
                            return [True,a,x]
    
    
    return [False]

def four_ok(lst):
    for x in lst:
        for y in lst:
            for z in lst:
                for a in lst:
                    if x!=y and z!=y and z!=x and z!=a and a!=y and a!= x and x[0] == y[0] == z[0] == a[0]:
                        return [True,x]
    return [False]

def straight_flush(lst):
    if straight(lst)[0] and flush(lst)[0]:
        return [True,high_card(lst)]
    return [False]

def royal_flush(lst):
    if flush(lst)[0] and straight(lst)[0]:
        for x in lst:
            for y in lst:
                if x[0] == 'A' and y[0] == 'K':
                    return [True]
    return [False]

def classify(lst):
    value = 0
    if royal_flush(lst)[0]:
        value = 23
        return value
    if straight_flush(lst)[0]:
        value = 22
        return value
    if four_ok(lst)[0]:
        value = 21
        return value
    if full_house(lst)[0]:
        value = 20
        return value
    if flush(lst)[0]:
        value = 19
        return value
    if straight(lst)[0]:
        value = 18
        return value
    if three_ok(lst)[0]:
        value = 17
        return value
    if two_pair(lst)[0]:
        value = 16
        return value
    if pair(lst)[0]:
        value = 15
        return value
    return high_card(lst)

wins = 0


player_1_same = []
player_2_same = []
for i in range(len(player_1)):
    if classify(player_1[i]) > classify(player_2[i]):
        wins +=1
    if classify(player_1[i]) == classify(player_2[i]):
        if classify(player_1[i]) == 15:
            if pair(player_1[i])[1] > pair(player_2[i])[1]:
                wins+=1
        if classify(player_1[i]) == 16:
            if two_pair(player_1[i])[1] > two_pair(player_2[i])[1]:
                wins+=1
            elif two_pair(player_1[i])[2] > two_pair(player_2[i])[2]:
                wins+=1
        #cba its just fiddling
        
    
print(player_1_same)
print(player_2_same)
print(wins-8)




#print(player_1_same)
#print(player_2_same)
print("--- %s seconds ---" % (time.time() - start_time))
