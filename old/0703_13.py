n, k = map(int, input().split())

l = [i for i in range(1, n + 1)]

# print(l)

count = 0
l2 = []
for i in range(len(l)):
    for j in range(len(l)):
        x = k - (l[i] + l[j])
        if x <= max(l) and [[l[i], l[j], x]] not in l2 and x !=0:
            l2.append([l[i], l[j], x])

print(len(l2))