n, x, y = map(int, input().split())

# print(n, x, y)

l = [i for i in range(1, n+1)]
# print(l)

for i in range(n):
    count = ""
    if l[i] % x == 0 and l[i] % y == 0:
        print("AB")
    elif l[i] % x == 0:
        print("A")
    elif l[i] % y == 0:
        print("B")
    else:
        print("N")