m, n = map(int, input().split())
l = [int(input()) for i in range(m)]
l2 = []
l3 = []
counts = 1
for i in range(m):
    l2 = []
    l2.append(n // l[i])
    l2.append(n % l[i])
    l2.append(counts)
    l3.append(l2)
    counts += 1
final = sorted(l3, key=lambda x:(x[1], x[0]))
print(final[0][2])