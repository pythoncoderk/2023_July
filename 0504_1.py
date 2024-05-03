a, b, n = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]

# print(a, b, n)
# print(l)

total = 0
for i in range(n-1):
    x = l[i+1][0] - l[i][1]
    train = a * 2
    hotel = b * x
    if train > hotel:
        total += hotel
    else:
        total += train
print(total + (a * 2))