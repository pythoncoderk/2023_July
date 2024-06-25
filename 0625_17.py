n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

strike = 0
ball = 0

for i in range(n):
    if l[i] == "strike":
        strike += 1
        if strike >= 3:
            print("out!")
        else:
            print("strike!")
    else:
        print("ball")