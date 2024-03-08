s = "lê quang hiếu "
str_phu = ""

while s != "":
    temp = s[:s.find(" ")].capitalize()
    str_phu = str_phu + temp + " "
    s = s[s.find(" ") + 1 :]

str_phu = str_phu[0:len(str_phu)-1]
print(str_phu)
