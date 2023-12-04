nk = list(input())
n = int(nk[0])
k = int(nk[1])
l = list(map(int, input().split()))
# print(n, k)
# print(l)
l2 = []
for i in range(n-k+1):
    l3 = []
    for j in range(k):
        l3.append(l[i+j])
    x = sum(l3)/k
    l2.append(x)
# print(l2)
p_max = max(l2)
p_count = l2.count(p_max)
start_day = l2.index(p_max)+1
# print(p_count)
# print(start_day)
print(f"{p_count} {start_day}")