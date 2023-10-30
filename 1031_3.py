n = int(input())
print("Hello ", end="")
l = [str(input()) for i in range(n)]
for i in range(n):
    if i == n-1:
        print(l[i], end=".")
    else:
        print(l[i], end=",")
