n = int(input())
l = list(map(int, input().split()))

# print(n)
# print(l)

answer = 0
for i in range(n):
    for j in range(n):
        if i != j:
            for k in range(n):
                if i != k and j != k:
                    if l[i] + l[j] + l[k] == 1000:
                        answer += 1

print("Yes" if answer >= 1 else "No")
