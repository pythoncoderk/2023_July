n, h, x = map(int, input().split())
l = list(map(int, input().split()))

# print(n, h, x)
# print(l)

l2 = [l[i] + h if l[i] + h >= x else 9999 for i in range(n)]
# print(l2)

min_l = min(l2)

for i in range(n):
    if min_l == l2[i]:
        print(i+1)
        break