x, y = map(int, input().split())
l = []
while x != 0:
    a = x % y
    l.insert(0, a)
    x = x // y
for i in l:
    print(i, end="")