x, y, n = map(int, input().split())

count = 0
sub_count = 1
a, b = 0, 0
now = "E"
l = ["E", "S", "W", "N"]
for i in range(n):
    if a == 0:
        if now == "E":
            x += 1
        elif now == "S":
            y += 1
        elif now == "W":
            x -= 1
        elif now == "N":
            y -= 1
