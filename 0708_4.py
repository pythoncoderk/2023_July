a, b = map(int, input().split())

x = a * b

for i in range(1, 4):
    if (x * i) % 2 != 0:
        print("Yes")
        exit()

print("No")