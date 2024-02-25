n = int(input())
l = [int(input()) for i in range(n)]

print(n)
print(l)

l2 = list(set(l[::]))
l2.sort(reverse=True)
print(l2)

l3 = []
for i in range(n):
    l3.append(l2.index(l[i])+1)

for i in range(n):
    if l3.count(l3[i]-1) == 1:
        print(l3[i])
    else:
        if l3.count(l3[i]-1) == 0:
            print(l3[i])
        else:
            print(l3.count(l3[i]) + i)
