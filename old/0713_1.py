s, t, x = map(int, input().split())


if t == 0:
    t = 24

if s < t:
    if s <= x < t:
        print("Yes")
    else:
        print("No")
elif s <= x < 23 or 0 <= x < t:
    print("Yes")

else:
    print("No")

