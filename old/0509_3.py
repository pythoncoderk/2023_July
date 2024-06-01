a, b = map(int, input().split())

l = [i for i in range(1, 7)]
print(l)

for i in range(6):
    x = 0
    for j in range(6):
        x = l[i] + l[j]
        if x == b:
            print("Yes")
            exit()
print("No")