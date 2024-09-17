n = int(input())

l = []
for i in range(n):
    b = input()
    if b == "ball":
        if l.count("ball") <= 2:
            print("ball!")
            l.append("ball")
        else:
            print("fourball!")
    else:
        if l.count("strike") <= 1:
            print("strike!")
            l.append("strike")
        else:
            print("out!")