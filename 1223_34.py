l = [int(input()) for i in range(30)]
if l.count(l[0]) == 30:
    print("YES")
else:
    print("NO")