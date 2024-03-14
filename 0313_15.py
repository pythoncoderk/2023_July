n = int(input())
l = [input() for i in range(n)]

for i in range(n-1, -1, -1):
    print(l[i])