n, x = map(int, input().split())

l = []
count = 65
for i in range(27):
    for j in range(n):
        l.append(chr(count))
    count += 1


print(l[x-1])