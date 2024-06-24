a, b = map(int, input().split())

x = a * b

count = 0
for i in range(1, 4):
    if (x * i) % 2 != 0:
        count += 1

print("Yes" if count >= 1 else "No")