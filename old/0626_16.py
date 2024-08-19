n = int(input())
l = [input() for i in range(n)]

strike = 0

for i in range(n):
    if l[i] == "strike":
        strike += 1
        print("strike!")
        print(strike)
    else:
        print("ball")