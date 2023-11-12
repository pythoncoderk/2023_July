x, y = map(int, input().split())
l = [input() for i in range(x)]
l2 = []
print(l)
for i in l:
    l2.append(i.replace("#", "."))
print(l2)