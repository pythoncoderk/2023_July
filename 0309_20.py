n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

x = 0
total = 0
while l:
    if x == 7:
        print(total, end=" ")
        x = 0
        total = 0
    else:
        total += l.pop(0)
        x += 1
print(total)