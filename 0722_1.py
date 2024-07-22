l = int(input())
u, a, b = map(int, input().split())
v = int(input())

usa_time = 0
usa_km = 0
while True:
    usa_km += 1
    usa_time += u

    if usa_km >= l:
        break

    if usa_km % a == 0:
        usa_time += b

kame_time = l * v

if kame_time == usa_time:
    print("DRAW")
elif kame_time < usa_time:
    print("KAME")
else:
    print("USAGI")
