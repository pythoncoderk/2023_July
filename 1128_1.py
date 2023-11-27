n, m = map(int, input().split())
a = [input() for i in range(n-2)]
c = [int(input()) for i in range(m)]
# print(n, m)
# print(a)
# print(c)
l = [i+1 for i in range(n-1)]
# print(l)
starts = 0
for i in range(m):
    starts += c[i]
    if a[i] == "x":
        pass
    elif a[i] == "+":
        starts += 1
    elif a[i] == "-":
        starts -= 1
    elif a[i] == "r":
        starts = 0
if starts >= n:
    print("goal")
    print(starts - n)
else:
    print("still")
    print(starts)