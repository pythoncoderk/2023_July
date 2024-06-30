n = int(input())
m = int(input())
l = [int(input()) for i in range(m)]

for i in range(m):
    if n == l[i]:
        print("first")
    elif n - 1 == l[i] or n + 1 == l[i]:
        print("adjacent")
    elif str(n)[-4:] == str(l[i])[-4:]:

        print("second")
    elif str(n)[-3:] == str(l[i])[-3:]:

        print("third")
    else:
        print("blank")