n = int(input())
m = int(input())

l = [i for i in range(1, n+1, m)]
# print(l)

chk = True
if l[1] % 2 == 0:
    chk = True

if n % 2 == 0 and m % 2 != 0:
    print("no")
elif chk:
    print("yes")
else:
    print("no")