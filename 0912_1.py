go = ["E", "S", "W", "N"]

x, y, n = map(int, input().split())
loop_count = 0
count = 1
one_two = 1
go_now = None
go_now_count = 0
while True:
    if one_two * 2 <= go_now_count:
        one_two = 1

    if go_now is None or go_now == "N":
        go_now = "E"
        x += 1
    elif go_now == "E":
        go_now = "S"
        y += 1
    elif go_now == "S":
        go_now = "W"
        x -= 1
    elif go_now == "W":
        go_now = "N"
        y -= 1
    go_now_count += 1

    if one_two >= 2:
        one_two = 0
        count += 1
        go_now_count = 0
    loop_count += 1
    if loop_count == n:
        break
print(x, y)

