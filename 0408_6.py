l = list(map(str, input().split()))
l[0] = int(l[0])
l[2] = int(l[2])

if l[1] == "+":
    print(l[0] + l[2])
elif l[1] == "-":
    print(l[0] - l[2])
elif l[1] == "*":
    print(l[0] * l[2])
elif l[1] == "/":
    if l[2] == 0:
        print("error")
    else:
        print(l[0] // l[2])
elif l[1] == "?" or l[0] == l[2] or l[1] == "!":
    print("error")