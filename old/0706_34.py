n, a, b = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, a, b)
# print(l)

l.insert(a, b)


for i in l:
    print(i)