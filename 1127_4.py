n, a, b = map(int,input().split())
l = [list(input()) for i in range(a)]
# print(n, a, b)
# print(l)
s = l[0].copy()
x = 0
while s != []:
    if l[1] == []:
        break
    else:
        if s[0] == l[1][x]:
            s.pop(0)
            l[1].pop(0)
        else:
            s.pop(0)
# print(l[1])
s = l[0].copy()
while s != []:
    if l[2] == []:
        break
    else:
        if s[0] == l[2][x]:
            s.pop(0)
            l[2].pop(0)
        else:
            s.pop(0)
# print(l[2])
one = len(l[1])
two = len(l[2])
print(f"{one} {two}")