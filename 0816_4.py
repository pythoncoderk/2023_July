n, k, m = map(int, input().split())

answer = 0
for i in range(n):
    x = int(input())
    if x >= k:
        answer += 1

print(answer - m if answer - m >= 0 else 0)