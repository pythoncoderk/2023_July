x, y = map(str, input().split())

x2 = 0
for i in range(len(x)):
    x2 += int(x[i])
x2 = str(x2)[-1]

y2 = 0
for i in range(len(y)):
    y2 += int(y[i])
y2 = str(y2)[-1]

if int(x2) > int(y2):
    print("Bob")
elif int(x2) == int(y2):
    print("Draw")
else:
    print("Alice")
