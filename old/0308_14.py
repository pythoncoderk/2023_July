n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

f = l[0][0]
last = l[-1][1]

h_l = [l[i][2] for i in range(n)]
low_l = [l[i][3] for i in range(n)]

print(f"{f} {last} {max(h_l)} {min(low_l)}")