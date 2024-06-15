n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = list(map(str, input().split()))

for i in range(n):
    l[i][1] = int(l[i][1])

main_time = int(m[1][:2])

for i in range(n):
    if l[i][0] == m[0]:
        main_time -= l[i][1]
main_minutes = m[1][-2:]

# print(n)
# print(l)
# print(m)
# print(main_time)

def times(x, y, z):
    if x + y < 0:
        xx = x + y + 24
    else:
        xx = x + y

    if xx >= 24:
        xx -= 24

    answer = str(xx).zfill(2)
    answer = answer + ":" + z
    return answer


for i in range(n):
    print(times(l[i][1], main_time, main_minutes))