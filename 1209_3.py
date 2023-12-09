n = int(input())
l = list(map(int, input().split()))
k = int(input())
# print(n)
# print(l)
# print(k)
if k in l:
    print(l.index(k)+1)
else:
    print(0)