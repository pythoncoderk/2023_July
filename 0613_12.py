n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

start = l[0][0]
end = l[n - 1][1]
hight = [l[i][2] for i in range(n)]
# print(hight)
low = [l[i][3] for i in range(n)]

print(start, end, max(hight), min(low))