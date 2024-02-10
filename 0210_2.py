import math

l = int(input())
u, a, b = map(int, input().split())
v = int(input())

# print(l)
# print(u, a, b)
# print(v)

kame = l * v
usa2 = (math.ceil(l / a)-1) * b
usa = (l * u) + usa2

if kame == usa:
    print("DRAW")
elif kame > usa:
    print("USAGI")
else:
    print("KAME")
