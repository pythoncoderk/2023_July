n = int(input())
l = list(map(int, input().split()))
k = int(input())
# print(n)
# print(l)
# print(k)
l.sort(reverse=True)
print(l[k-1])