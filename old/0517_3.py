a, b = map(int, input().split())

l = [i for i in range(1, 101) if 100 % i == 0]

# print(l)

l2 = [i for i in range(a, b+1)]

for i in range(len(l2)):
    if l2[i] in l:
        print("Yes")
        exit()

print("No")