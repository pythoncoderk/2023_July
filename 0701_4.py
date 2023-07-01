l = []
for _ in range(10):
    l.append(input())

for _ in range(10):
    if _ == 9:
        print(l[_])
    else:
        print(f"{l[_]} | ", end="")