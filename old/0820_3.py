a, b = map(int, input().split())

count = 0
while True:
    if a > b:
        print(count)
        break
    else:
        count += 1
        a += int(a * 0.1)