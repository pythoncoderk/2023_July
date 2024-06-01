a, b = map(int, input().split())
l = [i for i in range(1, 101) if 100 % i == 0]

# print(a, b)
# print(l)

l2 = [i for i in range(a, b + 1)]

for i in l2:
    if i in l:
        print("Yes")
        exit()

print("No")