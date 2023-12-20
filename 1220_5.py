n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
k = int(input())
l_m = [i for i in range(n) if k >= abs(l[i][0] - l[n-1][0]) + abs(l[i][1] - l[n-1][1])]

print(n)
print(l)
print(k)
print(len(l_m))