n = int(input())
l = [int(input()) for i in range(n)]
l.sort(reverse=True)

for i in l:
    print(i)