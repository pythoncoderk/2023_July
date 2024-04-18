n, m = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, m)
# print(l)

for i in range(n):
    if m == l[i]:
        pass
    elif m > l[i]:
        m += l[i] // 2
    elif m < l[i]:
        m = m // 2
print(m)