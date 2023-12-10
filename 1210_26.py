n = int(input())
l = [input() for i in range(n)]
print("Hello", end=" ")
for i in range(n):
    if i == n-1:
        print(l[i], end=".")
    else:
        print(l[i], end=",")