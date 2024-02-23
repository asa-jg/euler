def fib_gen(n):
    fib_lst = [1,2]
    while True:
        if fib_lst[-1] > n:
            fib_lst.pop(-1)
            return fib_lst
        else:
            fib_lst.append(fib_lst[-1] + fib_lst[-2])

final_lst = fib_gen(4000000)
print(final_lst)
final_lst2 = []
for i in range(len(final_lst)):
    if final_lst[i]%2 == 0:
        final_lst2.append(final_lst[i])

print (sum(final_lst2))
