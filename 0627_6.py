n = int(input())
l = list(map(int, input().split()))
q = int(input())
l2 = [int(input()) for i in range(q)]

print(n)
print(l)
print(q)
print(l2)

l_x = l[::]
i = 0
while i != n:
    m = len(l) // 2
    x = l[:m]
    y = l[m:]
    chk = False
    j = 0
    while (len(x) != 1 and len(y) != 1) and j < len(x):
        if l2[i] == x[j]:
            chk = True
            break
        else:
            j += 1
    if chk:
        l = x
    else:
        l = y

    if x == [] and y == []:
        print("No")
        i += 1
        l = l_x
    elif x == l2[i] or y == l2[i]:
        print("Yes")
        i += 1
        l = l_x
    else:
        print("No")
        i += 1
        l = l_x

