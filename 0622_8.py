a = int(input())
b = int(input())
n = int(input())

chk = True
while chk:
    if n % a == 0 and n % b == 0:
        chk = False
    else:
        n += 1
print(n)