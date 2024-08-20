n, m, k = map(int, input().split())

count = 0
while True:
    if n > k:
        print(count)
        break
    else:
        n += m
        count += 1