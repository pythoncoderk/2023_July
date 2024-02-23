n, m = map(int, input().split())
l = [int(input()) for i in range(m)]
l2 = [int(input()) for i in range(m)]
# print(n, m)
# print(l)
# print(l2)

l.sort()
l2.sort()

if l == l2:
    print("Yes")
else:
    print("No")
