n = int(input())
l = list(map(int, input().split()))
k = int(input())
x = 1
for i in l:
    if i == k:
        print(x)
        x += 1
    else:
        x += 1

