n = int(input())
l = list(map(int, input().split()))
l.sort()
# print(n)
# print(l)

total = 0
while l:
    x = l.pop(0)
    if l == []:
        total += x
    elif x+1 != l[0]:
        total += x
print(total)

