l = [int(input()) for i in range(5)]
l2 = []
for i in range(5):
    if i + 1 in l:
        l2.append(1)
if len(l2) >= 4:
    print("Yes")
else:
    print("No")