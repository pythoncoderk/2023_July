n = int(input())
m = int(input())

if m == 1:
    print("yes")
    exit()
if n == m:
    print("no")
    exit()

if n % 2 != 0:
    if n == m:
        print("no")
    else:
        print("yes")
else:
    if m % 2 == 0:
        print("no")
    else:
        print("yes")