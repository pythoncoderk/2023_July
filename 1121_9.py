l = list(input())
l2 = []
for i in l:
    l2.append(l.count(i))
if max(l2) >= 2:
    print("NG")
else:
    print("OK")