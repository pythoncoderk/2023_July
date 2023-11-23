n, v = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
# print(n, v)
# print(l)
yes_no = 0
for i in range(n-1):
    x = (l[i+1][1] - l[i][1]) // (l[i+1][0] - l[i][0])
    if x > v:
        yes_no += 1
if yes_no >= 1:
    print("YES")
else:
    print("NO")