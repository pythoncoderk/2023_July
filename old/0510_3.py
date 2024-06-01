l = [[2, 10], [3, 6], [9, 14]]
l2 = [0] * 15

for i in range(len(l)):
    l[i][0] -= 1

print(l)
print(l2)

for i in range(len(l)):
    l2[l[i][0]] += 1
    l2[l[i][1]] -= 1

print(l2)

x = 0
for i in range(len(l2)):
    l2[i] += x
    x = l2[i]
print(l2)