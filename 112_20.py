n = input()
x = n[1:]
l = list(x)
if len(l) == l.count(l[0]):
    print("Yes")
else:
    print("No")