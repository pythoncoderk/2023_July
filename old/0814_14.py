n = int(input())
l = [int(input()) for i in range(n)]
x, y = map(int, input().split())

l.insert(x, y)

for i in l:
    print(i)