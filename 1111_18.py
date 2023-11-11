n = int(input())
l = [int(input()) for i in range(n)]
l.sort()
l.reverse()
for i in l:
    print(i)