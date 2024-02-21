n = int(input())
l = [input() for i in range(2)]

# print(n)
# print(l)

count = 0
for i in range(n):
    if l[0][-1]+l[0][:-1] == l[1]:
        count += 1
    else:
        l[0] = l[0][-1]+l[0][:-1]

if count >= 1:
    print("Yes")
else:
    print("No")