x, y, n = map(int, input().split())
l = ["E", "S", "W", "N"]
if n == 0:
    print(x, y)
    exit()

for i in range(n):
    count = 0
    one = False
    two = False
    max_count = 1

    if not one:
        one = True
    elif not two:
        two = True


    if one and two:
        max_count += 1

    now_get = count % 4

    if now_get == 0:
        print("E")
    elif now_get == 1:
        print("S")
    elif now_get == 2:
        print("W")
    elif now_get == 3:
        print("N")