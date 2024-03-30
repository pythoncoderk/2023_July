n, k, q = map(int, input().split())

l = [int(input()) for i in range(n)]

# print(n, k, q)
# print(l)

l.insert(k, q)
for i in l:
    print(i)