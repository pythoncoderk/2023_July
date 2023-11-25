n = int(input())
m = int(input())
l = [i+1 for i in range(n)]
# print(l)
z = 0
for i in range(n):
    x = (m) + z
    if x > len(l):
        x = x-len(l)
    l[x-1] = "*"
    z = x
# print(l)

if l.count("*") == len(l):
    print("yes")
else:
    print("no")