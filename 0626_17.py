n = int(input())
l = [input() for i in range(n)]

strike = 0

for i in range(n):
    if l[i] == "ball":
        print("ball")
    else:
        strike += 1
        if strike >= 3:
            print("out!")
        else:
            print("strike!")