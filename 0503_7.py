n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

l2 = [l[i][0] + l[i][1] + (24 - l[i][2]) for i in range(n)]

# print(l2)

print(min(l2))
print(max(l2))