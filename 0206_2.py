n, k = map(int, input().split())
l = [int(input()) for i in range(n)]

# print(n, k)
# print(l)

cl = []
while k != 0:
    cl.append(k % 2)
    k //= 2

# print(cl)

for i in range(n):
    print(cl[l[i]-1])
