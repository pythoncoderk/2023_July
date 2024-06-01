n, m = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, m)
# print(l)

l2 = []
count = 0
while len(l2) != m:
    if l:
        l2.append(l.pop(0))
        l2 = set(l2)
        l2 = list(l2)
        count += 1
    else:
        break
if len(l2) == m:
    print(count)
else:
    print("unlucky")

