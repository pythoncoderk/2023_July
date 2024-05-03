n, m = map(int, input().split())
a, b, c = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, m)
# print(a, b, c)
# print(l)

l2 = [(l[i] * c) - a - (b * m) for i in range(n)]

l3 = [i for i in range(n) if l2[i] < 0]

print(len(l3))