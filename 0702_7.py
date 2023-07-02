l = []
for _ in range(10):
    l.append(input())

for i in range(10):
    if i == 9:
        print(l[i])
    else:
        print(l[i], end=" | ")