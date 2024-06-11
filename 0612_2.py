n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

def test(x):
    y = 1
    l2 = []
    while y < x:
        if x % y == 0:
            l2.append(y)
        y += 1
    return sum(l2)

for i in range(n):
    if test(l[i]) == l[i]:
        print("perfect")
    elif test(l[i]) - 1 == l[i] or test(l[i]) + 1 == l[i]:
        print("nearly")
    else:
        print("neither")