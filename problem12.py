from collections import Counter

start = timeit.default_timer()

b = 1; qty = 1; prf = []

while qty < 500:
    prf.clear(); qty = 1; num = int((b**2+b)/2)

    while num%2 == 0:
        prf.append(2)
        num /= 2
    f = 3
    while f*f <= num:
        if num%f == 0:
            prf.append(f)
            num /= f
        else:
            f += 2
    if num != 1:
        prf.append(int(num))

    cnt = Counter(prf)
    for i in cnt:
        qty *= cnt[i]+1

    b += 1

res = 1
for i in prf:
    res *= i

print(res)
