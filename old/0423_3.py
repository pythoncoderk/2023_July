n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
l2 = list(map(str, input().split()))
for i in range(n):
    l[i][1] = int(l[i][1])

times = l2[1].index(":")
times_h = int(l2[1][:times])

# print(n)
# print(l)
# print(l2)
# print(times_h)

d = {l[k][0]: l[k][1] for k in range(n)}
# print(d)

diff_time = times_h - d[l2[0]]
# print(diff_time)

for i in range(n):
    x = diff_time + l[i][1]
    if x >= 24:
        x -= 24
    elif x < 0:
        x += 24
    print(f"{str(x).zfill(2)}{l2[1][times:]}")