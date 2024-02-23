def length(num):
    return len(str(num))
fib_list= [0,1,1]

searching = True
i=2
while searching:
    fib_list.append(fib_list[i]+fib_list[i-1])
    i +=1
    if length(fib_list[-1])>=1000:
        searching = False
        print(i)