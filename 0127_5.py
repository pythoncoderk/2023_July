n = int(input())
q = list(map(int, input().split()))
l = [list(map(int, input().split())) for i in range(n)]
q2 = q[::]
a_count = 0
# print(q)
# print(l)
count = 0
while a_count <= 100000:
    for i in range(n):
        q2 = q[::]
        loop_count = 0

        for j in range(n):
            if q2[j] - l[i][j] < 0:
                a_count += 1
                break
            else:
                q2[j] -= l[i][j]
                loop_count += 1
        if loop_count == n:
            q = q2
            count += 1
print(count)