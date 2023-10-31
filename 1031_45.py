l = [int(input()) for i in range(5)]
while len(l) != 1:
    print(l[1] - l[0])
    l.pop(0)
