n = int(input())
l = [i+1 for i in range(n)]
x = l.pop(0)
while l != []:
    y = l.pop(0)
    x = x * y
counts = 0
while x % 2 == 0:
    x = x // 2
    counts += 1
print(counts)