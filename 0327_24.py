s, t = map(int, input().split())
h, m = map(int, input().split())

if s == h:
    if t >= m:
        print("Yes")
    else:
        print("No")
elif s > h:
    print("Yes")
else:
    print("No")