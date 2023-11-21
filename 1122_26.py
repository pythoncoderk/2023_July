import datetime

x, y = map(int, input().split())
a, b = map(int, input().split())

times1 = datetime.time(x, y)
times2 = datetime.time(a, b)

if times1 < times2:
    print("No")
else:
    print("Yes")


