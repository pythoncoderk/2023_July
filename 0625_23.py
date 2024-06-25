n, m = map(int, input().split())
p = int(input())
l = list(map(int, input().split()))
l2 = [int(input()) for i in range(m)]

# print(n, m)
# print(p)
# print(l)
# print(l2)

l3 = [l[i] for i in range(p) if l[i] % n == 0]

# print(l3)

for i in range(m):
    min_l = 999999999999999
    index_l = 0
    for j in range(len(l3)):
        if abs(l2[i] - l3[j]) <= min_l:
            min_l = abs(l2[i] - l3[j])
            index_l = j
    print(l3[index_l])