n = list(input())
l = []

for i in n:
    if i in l:
        pass
    else:
        l.append(i)
for i in l:
    print(i, end="")
