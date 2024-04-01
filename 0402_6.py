n, m = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, m)
# print(l)

l2 = []
count = 0
for i in range(n):
    if l[i] not in l2:
        l2.append(l[i])
        count += 1
    else:
        count += 1
    if len(l2) >= m:
        break
if len(l2) != m:
    print("unlucky")
else:
    print(count)
