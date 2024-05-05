a, b = map(int, input().split())
l = []
x = 1
while x <= 100:
    if 100 % x == 0:
        l.append(x)
    x += 1

# print(l)

l2 = [i for i in range(a, b+1)]
# print(l2)

for i in range(len(l2)):
    if l2[i] in l:
        print("Yes")
        exit()
print("No")