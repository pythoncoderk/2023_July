x, y, z = map(int, input().split())
n = list(map(int, input().split()))
n = n[x-1:y]
for i in n:
    print(i)