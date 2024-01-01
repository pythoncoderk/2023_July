x, y = map(int, input().split())
l = [input() for i in range(x)]
# print(x, y)
# print(l)
l2 = []
for i in l:
    l2.append(i[::-1])

l2_2 = l[::-1]

l3 = []
counter = -1
for i in range(x):
    r1 = l[counter][::-1]
    l3.append(r1)
    counter -= 1

if l == l2 and l == l3:
    print("line point symmetry")
elif l == l2 or l == l2_2:
    print("line symmetry")
elif l == l3:
    print("point symmetry")
else:
    print("none")