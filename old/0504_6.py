n = int(input())
m = int(input())

# print(n)
# print(m)

l = [i for i in range(1, n+1)]

# print(l)

l[0] = 0
x = m
count = 0
while sum(l) > 0:
    if count >= 10:
        print("no")
        exit()
    else:
        if l[x] != 0:
            l[x] = 0
            x += m
            if x >= n:
                x -= n
        else:
            print("no")
            exit()
print("yes")