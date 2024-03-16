l = list(map(int, input().split()))
# print(l)

taka = ((l[0] + l[2]) / l[1])
aoki = ((l[3] + l[5]) / l[4])

if taka == aoki:
    print("Draw")
elif taka < aoki:
    print("Takahashi")
else:
    print("Aoki")