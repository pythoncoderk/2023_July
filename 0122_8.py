n = int(input())
l = [int(input()) for i in range(n)]

# print(l)

for i in range(n):
    j = 1
    l2 = []
    while j < l[i]:
        if l[i] % j == 0:
            l2.append(j)
            j += 1
        else:
            j += 1
    if sum(l2) == l[i]:
        print("perfect")
    elif sum(l2) + 1 == l[i] or sum(l2) - 1 == l[i]:
        print("nearly")
    else:
        print("neither")