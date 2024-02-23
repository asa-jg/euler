tr = [1]; tl = [1]; br = [1]; bl = [1]

for i in range(1,501):
    tr.append(tr[-1] + 8*i)
    tl.append(tl[-1]+8*i-2)
    br.append(br[-1]+8*i-6)
    bl.append(bl[-1]+8*i-4)
print(sum(tr)+sum(tl)+sum(br)+sum(bl)-3)
