s = input()
s1 = s[::-1]
while s != s1:
    s = int(s) + int(s1)
    s = str(s)
    s1 = s[::-1]
print(s)