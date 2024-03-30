n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

for i in range(n):
    l2 = []
    for j in range(1, l[i]):
        if l[i] % j == 0:
            l2.append(j)
    if sum(l2) == l[i]:
        print("perfect")
    elif abs(sum(l2) - l[i]) == 1:
        print("nearly")
    else:
        print("neither")