n = int(input())
m = int(input())

x = 2
chk1 = True
while n != x+1:
    if n % x == 0:
        chk = False
        break
    else:
        x += 1

x = 2
chk2 = True
while m != x+1:
    if m % x == 0:
        chk2 = False
        break
    else:
        x += 1

if (chk1 or chk2) and n % m != 0:
    print("yes")
else:
    print("no")
