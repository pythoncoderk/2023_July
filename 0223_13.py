n = int(input())
m = int(input())

l = [0] * n
i = 0
count = 0
while count < n:
    l[i] = 1
    i += m
    count += 1
    if i >= n:
        i -= n

if len(l) == sum(l):
    print("yes")
else:
    print("no")