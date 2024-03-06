n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

taka = 0
for i in range(n):
    taka += l[i][0]

ao = 0
for i in range(n):
    ao += l[i][1]

if taka == ao:
    print("Draw")
elif taka > ao:
    print("Takahashi")
else:
    print("Aoki")