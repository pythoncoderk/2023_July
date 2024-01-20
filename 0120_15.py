n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
# print(l)
takahashi = 0
aoki = 0
for i in range(n):
    takahashi += l[i][0]
for i in range(n):
    aoki += l[i][1]

if takahashi > aoki:
    print("Takahashi")
elif takahashi < aoki:
    print("Aoki")
else:
    print("Draw")