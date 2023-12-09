n = int(input())
l = list(map(int, input().split()))
k = int(input())
# print(n)
# print(l)
# print(k)
l.reverse()
# print(l)
if k in l:
    l_index_r = l.index(k)
    final = n - l_index_r
    print(final)
else:
    print(0)