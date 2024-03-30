l = []

while True:
    x = int(input())
    if x == 0:
        l.append(x)
        break
    else:
        l.append(x)
l.reverse()
for i in l:
    print(i)