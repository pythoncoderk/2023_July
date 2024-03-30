n, y = map(int, input().split())

print(n, y)

l = []
for i in range(n+1):
    for j in range(n+1):
        l_x = []
        for k in range(n+1):
            l_x.append(i)
            l_x.append(j)
            l_x.append(k)
            if sum(l_x) == n and y == i * 10000 + j * 5000 + k * 1000:
                l = l_x
                print(f"{i} {j} {k}")
                exit()
            else:
                l_x = []
print(-1, -1, -1)


