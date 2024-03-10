n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
# print(n)
# print(l)

a = 0
b = 0

while l:
    a += l.pop(0)
    if l:
        b += l.pop(0)
print(a - b)