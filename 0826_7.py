points = 0

for _ in range(int(input())):
    x_counter = 0
    x,y = input().split()

    if x == y:
        points += 2
    else:
        if len(x) == len(y):
            for _ in range(len(x)-1):
                if x[_] != y[_]:
                    x_counter += 1
                else:
                    pass
            if x_counter == 1:
                points += 1
            else:
                pass
        else:
            pass
print(points)