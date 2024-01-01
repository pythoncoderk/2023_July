n = int(input())
l = [int(input()) for i in range(n)]
l2 = [l[i] for i in range(n) if l[i] % 2 != 0]
l2.sort()
for i in l2:
    print(i)
