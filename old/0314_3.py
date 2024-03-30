a, b = map(int, input().split())

def chk(x):
    if x == 1:
        y = [1]
    elif x == 2:
        y = [2]
    elif x == 3:
        y = [1, 2]
    elif x == 4:
        y = [4]
    elif x == 5:
        y = [1, 4]
    elif x == 6:
        y = [2, 4]
    elif x == 7:
        y = [1, 2, 4]
    elif x == 0:
        y = [0]
    return y


final = set(chk(a) + chk(b))
print(sum(final))