n, k, m = map(int, input().split())

total = 0
for i in range(n):
    x = int(input())
    if x >= k:
        total += 1

print(total - m if total - m >= 1 else 0)