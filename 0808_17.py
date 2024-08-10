n = int(input())
q = int(input())

l = [0] * n

for i in range(q):
    x, y = input().split()
    l[int(x) - 1] = y

k = input()

for i in l:
    if i == 0:
        print(k, end="")
    else:
        print(i, end="")