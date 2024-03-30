l = list(map(int, input().split()))
# print(l)

x = True
y = True
z = True

for i in range(len(l)-1):
    if l[i] > l[i+1]:
        x = False

for i in range(len(l)-1):
    if l[i] % 25 != 0:
        y = False

for i in range(len(l)-1):
    if 100 <= l[i] <= 675:
        pass
    else:
        z = False

if x and y and z:
    print("Yes")
else:
    print("No")