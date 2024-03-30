n, s, p = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
l2 = [l[i][0] if s - p <= l[i][1] <= s + p else 0 for i in range(n)]
# print(n, s, p)
# print(l2)

max_l = max(l2)
if max_l == 0:
    print("not found")
    exit()

for i in range(n):
    if max_l == l2[i]:
        print(i+1)
        break



