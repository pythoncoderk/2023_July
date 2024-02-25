n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

for i in range(1):
    print("Hello ", end="")
    for j in range(n):
        if j == n-1:
            print(l[j], end=".")
        else:
            print(l[j], end=",")


