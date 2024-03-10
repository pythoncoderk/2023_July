a = int(input())
b = int(input())
c = int(input())
x = int(input())

l = []
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            total = 0
            total += i * 500 + j * 100 + k * 50
            l.append(total)
print(l.count(x))