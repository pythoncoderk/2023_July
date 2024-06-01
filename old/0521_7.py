n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
m = input()

# print(n)
# print(l)
# print(m)

for i in range(n):
    if m == l[i][1]:
        print(l[i][0])