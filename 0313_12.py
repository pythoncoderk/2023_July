n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

f = 0
a = 0
for i in l:
    if i == "For":
        f += 1
    else:
        a += 1

if f > a:
    print("Yes")
else:
    print("No")