a, b = map(int, input().split())

count = 0
while a >= 1:
    a -= b
    count += 1
print(count)
