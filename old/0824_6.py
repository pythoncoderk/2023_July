max_x = 0

for i in range(100):
    for j in range(100):
        x = i
        y = j
        if (x ** 3) + (y ** 3) < 100000:
            max_x = max((x * y), max_x)

print(max_x)