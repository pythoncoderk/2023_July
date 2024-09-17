n = int(input())
strike_count = 0
ball_count = 0
for i in range(n):
    x = input()
    if x == "strike":
        strike_count += 1
        if strike_count <= 2:
            print("strike!")
        else:
            print("out!")
    else:
        ball_count += 1
        if ball_count <= 3:
            print("ball!")
        else:
            print("fourball!")
