s, t = map(str, input().split())

x = len(s)
y = len(t)
max_l = 0
if x == y:
    max_l = x
elif x > y:
    max_l = y
else:
    max_l = x

for i in range(max_l):
    if ord(s[i]) > ord(t[i]):
        print("No")
        exit()
    elif ord(s[i]) < ord(t[i]):
        print("Yes")
        exit()

if x < y:
    print("Yes")
else:
    print("No")

