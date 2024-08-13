n = int(input())
l = [int(input()) for i in range(n)]
x, y = map(int, input().split())

l[x - 1], l[y - 1] = l[y - 1], l[x - 1]

for i in l:
    print(i)