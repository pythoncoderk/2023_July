h = int(input())

chk = False
x = 0
count = 1
while chk == False:
    y = (x * 2) + 1
    if y > h:
        chk = True
    else:
        x = y
        count += 1

print(count)