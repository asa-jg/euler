import time
start_time = time.time()

for i in range(13800000000,10000000000000):
    val = str((10*i)**2)
    if len(val) == 18:
        if val[0] == '1' and val[2] == '2' and val[4] == '3' and val[6] == '4' and val[8] == '5' and val[10] == '6' and val[12] == '7' and val[14] == '8' and val[16] == '9' and val[18] == '0':
            print(i)
            print("--- %s seconds ---" % (time.time() - start_time))
            quit()
print('pop')

