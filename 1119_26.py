l = list(map(int, input().split()))
l2 = list(map(int, input().split()))

x = l[2] / (l[0] * l[1])
y = l2[2] / (l2[0] * l2[1])

if x < y:
    print(f"{l[0]} {l[1]} {l[2]}")
elif x == y:
    print("DRAW")
else:
    print(f"{l2[0]} {l2[1]} {l2[2]}")