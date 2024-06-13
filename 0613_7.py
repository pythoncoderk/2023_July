a, b = map(int, input().split())

x = 1
y = 1

count = 0
while a != x or b != y:
    if x == y:
        count += 1
    y += 1
    if y > b:
        x += 1
        y = 1
print(count + 1 if a == b else count)