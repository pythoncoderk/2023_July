l = list(map(int, input().split()))
l.sort(reverse=True)

for i in range(len(l)):
    l[i] = str(l[i])

x = int(l[0] + l[1])
y = int(l[2])

print(x + y)
