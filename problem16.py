def convert(num):
    li = [int(x) for x in str(num)]
    return li

num = 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
print(sum(convert(num)))