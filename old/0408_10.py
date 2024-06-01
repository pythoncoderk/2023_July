import math

n = int(input())
m = int(input())

l = [list(map(str, input().split())) for i in range(n)]
for i in range(n):
    l[i][1] = int(l[i][1])

# print(n)
# print(m)
# print(l)

for i in range(n):
    if l[i][0] == "+":
        m += l[i][1]
        print(i+1, m)
    elif l[i][0] == "-":
        m -= l[i][1]
        print(i+1, m)
    elif l[i][0] == "*":
        m *= l[i][1]
        print(i+1, m)
    elif l[i][0] == "/":
        if l[i][1] == 0:
            print("error")
            exit()
        else:
            m //= l[i][1]
            print(i+1, int(m))
