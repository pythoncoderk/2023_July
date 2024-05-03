n, m = map(int, input().split())
l = [int(input()) for i in range(m)]
l2 = [int(input()) for i in range(m)]

# print(n, m)
# print(l)
# print(l2)

l.sort()
l2.sort()

one = ""
for i in range(m):
    one += str(l[i])

two = ""
for i in range(m):
    two += str(l2[i])

if one == two:
    print("Yes")
else:
    print("No")