import copy

n = int(input())
m = int(input())
l = [int(input()) for i in range(m)]
n2 = copy.copy(n)
n2 = str(n2)
l2 = copy.copy(l)
l2 = str(list(l2))
print(l)
print(l2)
print(n)
print(n2)
print(l2[0])
for i in range(m):
    if l[i] == n:
        print("first")
    elif l[i] == n - 1 or l[i] == n + 1:
        print("adjacent")
    elif l2[i][-4:] == n2[i][-4:]:
        print("second")
    elif l2[i][-3:] == n2[i][-3:]:
        print("third")
    else:
        print("blank")
