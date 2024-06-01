d = int(input())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

print(d)
print(n)
print(l)

l2 = d * [0]

print(l2)

for i in range(n):
    l2[l[i][0]-1] += 1
    l2[l[i][1]] -= 1

print(l2)

xxx = 0
for i in range(d):
    xxx += l2[i]
    print(xxx)