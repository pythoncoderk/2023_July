n = int(input())
m = int(input())

l = [1 if i == 0 else 1 for i in range(n)]

x = 0
while sum(l) != 0:
    if l[x] == 0:
        print("no")
        exit()
    else:
        l[x] = 0
        x += m
        if x >= n:
            x -= n

print("yes")