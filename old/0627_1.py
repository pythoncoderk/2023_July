n, m = map(int, input().split())
p = int(input())
l = list(map(int, input().split()))
l2 = [int(input()) for i in range(m)]

# print(n, m)
# print(p)
# print(l)
# print(l2)

l = [l[i] for i in range(p) if l[i] % n == 0]

# print(l)

for i in range(m):
    min_l = 999999999
    index_l = 0
    for j in range(len(l)):
        if min_l >= abs(l2[i] - l[j]):
            min_l = abs(l2[i] - l[j])
            index_l = j
    print(l[index_l])