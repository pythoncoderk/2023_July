n = int(input())
d = {input(): 0 for i in range(n)}

m = int(input())
for i in range(m):
    x = input().split()
    d[x[0]] += int(x[1])

print(d[input()])