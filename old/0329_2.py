a, b = map(str, input().split())

a = list(a)
b = list(b)

# print(a)
# print(b)

max_s = 0
if len(a) == len(b):
    max_s = len(a)
elif len(a) > len(b):
    max_s = len(a)
else:
    max_s = len(b)

# print(max_s)

l_f = []
for i in range(max_s):
    if a:
        x = int(a.pop(-1))
    else:
        x = 0

    if b:
        y = int(b.pop(-1))
    else:
        y = 0
    l_f.append(str(x + y)[-1])
l_f.reverse()
for i in range(len(l_f)):
    print(l_f[i], end="")