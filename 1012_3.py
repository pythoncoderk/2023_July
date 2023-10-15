n = int(input())
l = list(map(int, input().split()))
l.sort()
final = set(l)
for i in range(len(final)):
    if i+1 == final:
        print(final[i])
    else:
        print(final[i], end=" ")