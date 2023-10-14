import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

so_ban = math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2)


print("Số bàn tối thiểu cần mua là:", so_ban)