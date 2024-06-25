n = int(input())
l = [input() for i in range(n)]

ball = 0
strike = 0

for i in range(n):
    if l[i] == "ball":
        ball += 1
        if ball >= 4:
            print("fourball!")
        else:
            print("ball!")
    else:
        strike += 1
        if strike >= 3:
            print("out!")
        else:
            print("strike!")