l = [int(input()) for i in range(2)]
if l[1] % l[0] == 0:
    print(l[1] // l[0])
else:
    print((l[1] // l [0]) + 1)