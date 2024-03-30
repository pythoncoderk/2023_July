a, b, c = map(int, input().split())

l = [i for i in range(a, b+1)]
# print(l)

count = 0
l2 = []
for i in range(len(l)):
    if l[i] % c == 0:
        count += 1
        l2.append(l[i])

if count == 0:
    print(-1)
else:
    print(l2[0])