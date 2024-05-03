n, m = map(int, input().split())
l = list(map(int, input().split()))

# print(n, m)
# print(l)

for i in range(n - m + 1):
    l2 = []
    for j in range(i, i + m):
        l2.append(l[j])
    if sum(l2) == 0:
        print("NG")
        exit()
print("OK")