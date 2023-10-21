n = int(input())
l = []
while n != 0:
    x = n % 2
    l.insert(0, x)
    n = n // 2
for i in l:
    print(i, end="")



