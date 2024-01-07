n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
l2 = [l[i][0] * l[i][1] if l[i][0] == l[i][1] else l[i][0] + l[i][1] for i in range(n)]
print(sum(l2))