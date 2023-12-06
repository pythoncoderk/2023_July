n = int(input())
l = list(map(int, input().split()))
l.reverse()
# print(l)
for i in range(n):
    if l[i] % 2 == 1:
        print(len(l) - i)
        break