q = int(input())
l = [list(map(int, input().split())) for i in range(q)]

# print(q)
# print(l)

q_l = []
for i in range(q):
    if l[i][0] == 1:
        if len(q_l) == 0:
            q_l.append(l[i][1])
        elif q_l[0] > l[i][1]:
            q_l.insert(0, l[i][1])
        else:
            q_l.append(l[i][1])
    elif l[i][0] == 2:
        print(q_l[0])
    else:
        q_l.pop(0)