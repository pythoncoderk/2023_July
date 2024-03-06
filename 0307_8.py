s = input()
n = int(input())
l = [input() for i in range(n)]

# print(s)
# print(n)
# print(l)

l2 = []
for i in range(n):
    if s not in l[i]:
        l2.append(l[i])

if not l2:
    print("none")
else:
    for i in l2:
        print(i)