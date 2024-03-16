l = list(map(int, input().split()))
x = l[0]
l2 = l[1:]
# print(x)
# print(l2)
count = 0
index_l = 0
while x >= 0:
    if count >= 3:
        count = 0
    x -= l2[count]
    count += 1
count -= 1

if count == 0:
    print("F")
elif count == 1:
    print("M")
else:
    print("T")