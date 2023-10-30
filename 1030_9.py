n, m = map(int, input().split())
l = [int(input()) for i in range(n)]
for i in range(m):
    if l != []:
        print(l.pop(0))
    else:
        print(0)