l = list(map(int, input().split()))
l2 = list(map(int, input().split()))
if l[2] / (l[0] * l[1]) == l2[2] / (l2[0] * l2[1]):
    print("DRAW")
elif l[2] / (l[0] * l[1]) < l2[2] / (l2[0] * l2[1]):
    print(f"{l[0]} {l[1]} {l[2]}")
else:
    print(f"{l2[0]} {l2[1]} {l2[2]}")