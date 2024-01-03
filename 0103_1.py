n = int(input())
l = [input() for i in range(n)]
l2 = []

for i in l:
    if i == "strike":
        if l2.count("strike") >= 2:
            print("out!")
        else:
            print("strike!")
            l2.append("strike")
    else:
        if l.count("ball"):
            if l2.count("ball") >= 3:
                print("fourball!")
            else:
                print("ball!")
                l2.append("ball")