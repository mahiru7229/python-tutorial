n = int(input("Số học sinh: n = "))
k = int(input("Số mận:      k = "))

moi_hs = k//n
con_du = k % n


print("Mỗi học sinh được chia",moi_hs,"quả mận.")
print("Số mận dành riêng cho các em nữ là", con_du)