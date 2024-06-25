n, m = map(int, input().split())
x = int(input())

y = n
count = 0
while True:
    if n + y >= 1500:
        break
    else:
        if count == 0:
            answer = n
            count += 1
        else:
            answer = n + y
            n += y

    print(answer, abs(answer - x))

print()