n = int(input())
l = []
for i in range(n):
    x = input()
    l.append(x)
    if x == "strike":
        print("strike!")
        print(l.count("strike"))
    else:
        print("ball")