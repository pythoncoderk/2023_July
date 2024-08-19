n = int(input())

l = [int(input()) for i in range(n)]

x = int(input()) - 1

for i in range(n):
    if i == x:
        del l[i]
        break

for i in l:
    print(i)