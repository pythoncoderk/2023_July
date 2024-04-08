n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

i = 0
while i < n:
    print(l[i][0] + l[i][1])
    i += 1