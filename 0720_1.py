n = int(input())
l = [int(input()) for i in range(n)]
l2 = []
for x in range(n):
    answer = [i for i in range(1, l[x] + 1) if l[x] % i == 0]
    l2.append(answer)

for i in range(n):
    if sum(l2[i]) == l2[i][-1] * 2:
        print("OK")
    elif abs(sum(l2[i]) - l2[i][-1] * 2) == 1:
        print("近い")
    else:
        print("全然違う")