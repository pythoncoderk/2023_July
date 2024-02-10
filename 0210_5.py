n, m = map(int, input().split())
l = [int(input()) for i in range(m)]

# print(n, m)
# print(l)
point = 0
for i in range(m):

    if point >= l[i]:
        point -= l[i]

    else:
        n -= l[i]
        point += l[i] // 10
    print(f"{n} {point}")
