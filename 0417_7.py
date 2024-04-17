n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

x = 0
up = []
for i in range(n-1):
    if l[i] < l[i+1]:
        x += 1
        up.append(x)
    else:
        x = 0
        up.append(x)


y = 0
down = []
for i in range(n-1):
    if l[i] > l[i+1]:
        y += 1
        down.append(y)
    else:
        y = 0
        down.append(y)

print(f"{max(down)} {max(up)}")