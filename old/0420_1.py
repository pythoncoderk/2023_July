n, m = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, m)
# print(l)

for i in range(n):
    if l[i] < m:
        m += l[i] // 2
    elif l[i] > m:
        m = m // 2

print(m)