a, d, a = map(int, input().split())
n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
print(l)
l2 = []
for i in range(n):
    ll = []
    for j in range(6):
        if j != 0:
            ll.append(int(l[i][j]))
        else:
            ll.append(l[i][j])
        l2.append(ll)
print(l2)
