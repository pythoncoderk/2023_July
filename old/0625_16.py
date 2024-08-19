n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

ball = 0
strike = 0

for i in range(n):
    if l[i] == "ball":
        ball += 1
        print("ball")
    else:
        strike += 1
        print("strike!")
        print(strike)