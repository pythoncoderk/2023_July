n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

s = l[0][0]
last = l[-1][1]

l_higt = l[0]
for i in range(n):
    l_higt += l[i]
# print(l_higt)

l_h = max(l_higt)
l_low = min(l_higt)

print(f"{s} {last} {l_h} {l_low}")
