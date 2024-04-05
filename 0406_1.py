n, a, b = map(int, input().split())
l = [list(input()) for i in range(3)]

# print(n, a, b)
# print(l)

while l[0]:
    x = l[0].pop(0)
    if l[1]:
        if l[1][0] == x:
            del l[1][0]
    if l[2]:
        if l[2][0] == x:
            del l[2][0]

print(len(l[1]), len(l[2]))