n, x, y = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, x, y)
# print(l)
stocks = []
total = 0
for i in range(n):
    if i == n-1:
        for p in stocks:
            total += l[i]-p

    else:
        if l[i] <= x:
            stocks.append(l[i])
        elif l[i] >= y:
            for j in stocks:
                total += l[i]-j
            stocks = []
print(total)

