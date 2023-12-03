l = int(input())
u, a, b = map(int, input().split())
v = int(input())
# print(l)
# print(u, a, b)
# print(v)
kame = l * v
# print(kame)
usagi_km = l
usagi_time = 0
usagi_go = 0
while usagi_km > 0:
    usagi_km -= 1
    usagi_go += 1
    usagi_time += u
    if usagi_go % a == 0 and usagi_km > 0:
        usagi_time += b

# print(usagi)

if kame == usagi_time:
    print("DRAW")
elif kame < usagi_time:
    print("KAME")
elif kame > usagi_time:
    print("USAGI")
