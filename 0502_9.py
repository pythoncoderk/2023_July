n = input()
chk = True
while chk:
    x = n[::-1]
    if x == n:
        chk = False
    else:
        n = int(n) + int(x)
        n = str(n)
print(x)