n = int(input())
while n >= 2:
    x = n / 2
    n = x
if n == 1.0:
    print("OK")
else:
    print("NG")