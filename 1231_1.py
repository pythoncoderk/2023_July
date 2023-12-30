n = int(input())
l = [int(input()) for i in range(n)]

l2 = []
x = 1
while l != []:
    if x == l[0]:
        xx = l.pop(0)
        x = 1
        total = sum(l2)
        if xx == total:
            print("ppp")
        elif xx - 1 == total:
            print("n1")
        else:
            print("n2")
        l2 = []
    else:
        if l[0] % x == 0:
            l2.append(x)
            x += 1
        else:
            x += 1
