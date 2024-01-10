n, k, q = map(int, input().split())
l = [int(input()) for i in range(n)]
l.insert(k, q)
# print(n, k, q)
for i in l:
    print(i)