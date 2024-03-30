n, a, b = map(int, input().split())
l = list(map(int, input().split()))

# print(n, a, b)
# print(l)

x = a + b
for i in range(n):
    if l[i] == x:
        print(i+1)
