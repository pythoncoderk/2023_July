a, b = map(int, input().split())

l = [i for i in range(a, b + 1)]

# print(l)

l2 = [i for i in range(1, 101) if 100 % i == 0]

# print(l2)


for i in range(len(l)):
    for j in range(len(l2)):
        if l[i] in l2:
            print("Yes")
            exit()

print("No")