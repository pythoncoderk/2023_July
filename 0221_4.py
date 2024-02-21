n, c = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(n, c)
# print(l)

count = 0
k_calory = 0
for i in range(n):
    if k_calory >= c:
        break
    else:
        if l[i][0] <= 10:
            count += 1
        k_calory += l[i][1]
if count >= 10:
    print("Yes")
else:
    print(count)