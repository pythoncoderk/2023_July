n, k = map(int, input().split())
l = [int(input()) for i in range(n*k)]
# print(n, k)
# print(l)
l4 = []
l3 = []
count = 0
for i in range((n*k)-k):
    l2 = []
    for j in range(k):
        l2.append(l[j+i])
    l3.append(sum(l2)/k)
    count += 1
    if count == k:
        l4.append(min(l3))
        l3 = []
        count = 0
print(l4.index(min(l4))+1)
