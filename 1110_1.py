n = int(input())
l = list(map(int, input().split()))
for i in range(n-1):
    x = l[:i+1]
    if l[i] in x:
        print("Yes")
    else:
        print("No")