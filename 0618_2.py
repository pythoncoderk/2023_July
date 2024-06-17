n = list(map(str, input().split()))

# print(n)

index_x = n.index("x")

for i in range(5):
    if n[i] != "x" and n[i] != "=" and n[i] != "+" and n[i] != "-":
        n[i] = int(n[i])

# print(index_x)

if index_x == 4:
    if n[1] == "+":
        print(n[0] + n[2])
    else:
        print(n[0] - n[2])
elif index_x == 0:
    if n[1] == "+":
        print(n[4] - n[2])
    else:
        print(n[4] + n[2])
else:
    if n[1] == "+":
        print(n[4] - n[0])
    else:
        print((n[4] - n[0]) * -1)