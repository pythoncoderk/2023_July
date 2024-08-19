n = int(input())

total_1 = 0
total_2 = 0
for i in range(n):
    x, y = input().split()
    x1 = int(x[:2])
    x2 = int(x[3:])

    y1 = int(y[:2])
    y2 = int(y[3:])
    time_1 = y1 - x1
    time_2 = y2 - x2

    if time_2 < 0:
        time_1 -= 1
        time_2 += 60
    total_1 += time_1
    total_2 += time_2



    if total_2 >= 60:
        total_1 += total_2 // 60
        total_2 = total_2 % 60

print(total_1, total_2)
