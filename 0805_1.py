


points = 0
all_points2 = 0
def diff(x, y):
    points = 0
    all_points2 = 0
    for _ in range(len(x)):
        if x[_] == y[_]:
            pass
        else:
            points += 1
    if points == 1:
        all_points2 = 1
    else:
        pass

n = int(input())
l = []
for i in range(n):
    l.append(input().split())

print(l)
all_points = 0
for _ in range(n):
    if l[_][0] == l[_][1]:
        all_points += 2
    elif len(l[_][0]) == len(l[_][1]):
        diff(l[_][0],l[_][1])
        if points == 1:
            all_points += 1
        else:
            pass
    else:
        pass

print(all_points + all_points2)