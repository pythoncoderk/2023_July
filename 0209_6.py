n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

ball = 0
strike = 0

for i in range(n):
    if l[i] == "ball":
        if ball <= 2:
            print("ball!")
            ball += 1
        else:
            print("fourball!")
    else:
        if strike <= 1:
            print("strike!")
            strike += 1
        else:
            print("out!")
