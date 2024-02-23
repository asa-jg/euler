coins = []

divisor = 4503599627370517
smallest = 4503599627370517
a = 1504170715041707
i = 1
searching = True
while searching:
    if (i*a)%divisor in coins:
        searching = False
    if (i*a)%divisor < smallest:
        smallest = (i*a)%divisor
        coins.append((i*a)%divisor)
        print(smallest)
    i +=1
print(sum(coins))
    