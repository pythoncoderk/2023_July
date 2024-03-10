n, a, b = map(int, input().split())

l = [i for i in range(1, n+1)]
# print(l)

total = []
for i in range(len(l)):
    x = list(str(l[i]))
    for j in range(len(x)):
        x[j] = int(x[j])
    if a <= sum(x) <= b:
        total.append(l[i])
print(sum(total))