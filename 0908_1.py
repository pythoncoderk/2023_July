n = int(input())
l = []
for i in range(n):
    l.append(input())
print("TEST ", end="")

for i in l:
    if i == l[-1]:
        print(i, end=".")
    else:
        print(i, end=",")