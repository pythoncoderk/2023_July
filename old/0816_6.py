n = int(input())

l = [int(input()) for i in range(n)]

diff = 999
x = 0
y = 0
for i in range(len(l)):
    diff_1 = 0
    for j in range(i + 1, len(l)):
        diff_1 = abs(l[i] - l[j])
        if diff > diff_1:
            diff = diff_1
            x = l[i]
            y = l[j]

if x > y:
    print(y)
    print(x)
else:
    print(x)
    print(y)