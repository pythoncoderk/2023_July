n, k = map(int, input().split())
l = [int(input()) for i in range(n)]
l.sort()

# print(n, k)
# print(l)

l2 = [abs(l[i] - k) for i in range(n)]

# print(l2)

min_l = min(l2)

l3 = [l[i] for i in range(n) if l2[i] == min_l]
l3.sort()

for i in l3:
    print(i)

