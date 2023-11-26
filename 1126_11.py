n = int(input())
l = [int(input()) for i in range(n)]
l2 = [list(map(int, input().split())) for i in range(n)]
m = int(input())
l3 = [int(input()) for i in range(m)]
# print(n)
# print(f"滞在時間{l}")
# print(f"時刻表  {l2}")
# print(m)
# print(l3)
l4 = []
for i in range(m):
    l4.append(l[l3[i]-1])
for i in range(m-1):
    l4.append(l2[l3[i]-1][l3[i+1]-1])
print(sum(l4))