n = int(input())

x = 0
while x <= n:
    if n == pow(2, x):
        print("OK")
        exit()
    else:
        x += 1
print("NG")