l = list(map(int, input().split()))

l.sort(reverse=True)

x = str(l[0]) + str(l[2])
y = str(l[1]) + str(l[3])

print(int(x) + int(y))

