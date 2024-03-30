l = int(input())
u, a, b = map(int, input().split())
v = int(input())

# print(l)
# print(u, a, b)
# print(v)

kame = v * l
usa = (l * u) + (((l / a)-1) * b)

if kame == usa:
    print("DRAW")
elif kame > usa:
    print("USAGI")
else:
    print("KAME")
