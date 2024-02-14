n = int(input())
l = list(map(int, input().split()))
l.sort()

# print(n)
# print(l)
final = []
while l:
    if len(l) == 1:
        break
    x = l.pop(0)
    if x + 1 != l[0]:
        final.append(x)
print(sum(final) + l[0])

