a, b = map(int, input().split())
s = a ^ b
c = a & b

print(f"{c} {s}")