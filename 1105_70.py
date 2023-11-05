import datetime

x, y = map(int, input().split())
a, b = map(int, input().split())
x2 = str(x) + str(y)
a2 = str(a) + str(b)
t1 = datetime.datetime.strptime(x2, "%H%M")
t2 = datetime.datetime.strptime(a2, "%H%M")

if t1 >= t2:
    print("Yes")
else:
    print("No")