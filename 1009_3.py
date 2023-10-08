n = int(input())
for i in range(n):
    if i + 1 == int(n/2) or i+1 == n:
        print(i+1)
    else:
        print(i+1, end=" ")
