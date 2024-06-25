n = int(input())

l = [input() for i in range(n)]

# print(n)
# print(l)

ball = 0
strike = 0

for i in range(n):
    if l[i] == "ball":
        ball += 1
        if ball <= 3:
            print("ball!")
        else:
            print("fourball!")
    if l[i] == "strike":
        strike += 1
        if strike <= 2:
            print("strike!")
        else:
            print("out!")