xau = input("Nhập xâu: ")
ds_chu_so = []
for i in range(len(xau)):
    if (xau[i] >= '0' and xau[i] <= '9'):
        ds_chu_so.append(xau[i])

for i in ds_chu_so:
    print(i, end=" ")
    
    
