n = int(input())
ball = []
strike = []
for i in range(n):
    if input() == "ball":
        if len(ball) >= 3:
            print("fourball!")
        else:
            print("ball!")
            ball.append(1)
    else:
        if len(strike) >= 2:
            print("out!")
        else:
            print("strike!")
            strike.append(1)