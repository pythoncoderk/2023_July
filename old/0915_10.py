n = int(input())
l = list(map(int, input().split()))

answer = False
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and i != k:
                if l[i] + l[k] + l[j] == 1000:
                    answer = True

print("Yes" if answer else "No")