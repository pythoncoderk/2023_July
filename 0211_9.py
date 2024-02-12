import copy

n, A, B = map(int, input().split())
l = [list(input()) for i in range(A)]
l2 = copy.deepcopy(l)
# print(n, a, b)
# print(l)

while l2[0]:
    if len(l2[1]) != 0:
        if l2[0][0] == l2[1][0]:
            del l2[1][0]
        del l2[0][0]
    else:
        break
# print(l2)

x = len(l2[1])

l3 = copy.deepcopy(l)
while l3[0]:
    if len(l3[2]) != 0:
        if l3[0][0] == l3[2][0]:
            del l3[2][0]
        del l3[0][0]
    else:
        break
# print(l3)

y = len(l3[2])

print(f"{x} {y}")



















