n, d = map(int, input().split())
l = [int(input()) for i in range(n-1)]
# print(n, d)
# print(l)
l2 = [d]
for i in l:
    l2.append(d - i)
# print(l2)

print(d * sum(l2))