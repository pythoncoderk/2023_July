n = int(input())
l = [input() for i in range(n)]

for i in range(n):
    if l[i] == "ball":
        print("ball")
    else:
        print("strike!")