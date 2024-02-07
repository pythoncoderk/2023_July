import math

n, m, t, k2 = map(int, input().split())
print(n, m, t, k2)

l = [list(map(int, input().split())) for i in range(m)]
print(l)
x = 0
count_l = []
for i in range(m-t):
    x = 0
    for j in range(m-t+1):
        count = 0
        for k in range(x, x+t):
            count += l[k][i]
        count_l.append(count)
        x += 1
    max_count = 0
    for xxx in range(len(count_l)):
        if count_l[xxx] >= k2:
            max_count = m - xxx
            break
    if max_count == 0:
        print("no 0")
    else:
        print(f"yes {max_count}")
    count_l = []
