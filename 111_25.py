n = input()
l = list(n)
if len(l) == l.count(l[0]):
    print(n)
else:
    print("No")