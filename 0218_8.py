n, s, d = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, s, d)
# print(l)

count = 0
for i in range(n):
    if l[i][0] < s and l[i][1] > d:
        count += 1
if count >= 1:
    print("Yes")
else:
    print("No")