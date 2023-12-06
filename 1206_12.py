n = int(input())
l = list(map(int, input().split()))
m = int(input())

for i in range(n):
    if l[i] == m:
        print(i+1)