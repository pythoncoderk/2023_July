n = int(input())

count = 0
l = []
while n != 0:
    n -= 1
    l.append(1)
    count += 1

print(count)
for i in l:
    print(i)