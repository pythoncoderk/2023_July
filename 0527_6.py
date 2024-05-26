
n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)

deque_l = []

for i in range(n):
    if l[i][0] == "1":
        deque_l.append(l[i][1])
    elif l[i][0] == "2":
        print(deque_l[0])
    elif l[i][0] == "3":
        deque_l.pop(0)
