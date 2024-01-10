d, n, l = map(int, input().split())
li = [int(input()) for i in range(n)]
li.insert(0, 0)
# print(d,n,l)
# print(li)
total = 0
for i in range(n):
    if li[i+1] - li[i] >= 0:
        total += li[i+1] - li[i]

if total < l:
    print("Yes")
else:
    print("No")