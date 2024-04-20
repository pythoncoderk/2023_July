s = input()

l = []
for i in range(1, 350):
    if i != 316:
        l.append("ABC" + str(i).zfill(3))

if s in l:
    print("Yes")
else:
    print("No")