l1, r1, l2, r2 = map(int, input().split())

s1 = {i for i in range(l1, r1 + 1)}
s2 = {i for i in range(l2, r2 + 1)}

# print(s1)
# print(type(s1))
#
# print(s2)
# print(type(s2))

answer = s1 & s2
#
# print(answer)

if len(answer) == 0:
    print(0)
else:
    if len(answer) - 1 < 0:
        print(0)
    else:
        print(len(answer) - 1)