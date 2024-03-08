

s = input()
count = 0



for i in range(len(s)):
    if s[i].isalpha():
        count = count + 1
print(count)

