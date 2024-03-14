n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

x = max(l)
print(l.index(x)+1)
