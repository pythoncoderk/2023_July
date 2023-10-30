n = int(input())
l = [int(input()) for i in range(n)]
m = int(input())
l.pop(m-1)
for i in l:
    print(i)
