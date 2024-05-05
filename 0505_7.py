n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

anser = False
for i in range(n):
    for j in range(n):
        if i != j:
            for k in range(n):
                if i != k and j != k:
                    x = l[i] + l[j] + l[k]
                    if x == 1000:
                        anser = True
                        break

if anser:
    print("Yes")
else:
    print("No")