n = int(input())
a, b = map(int, input().split())
p = 1
k = 1
counts_p = 0
p_counts = 0
while n >= k:
    if p_counts == 0:
        k = (p * a) + k
        p_counts = 1
        counts_p += 1
    else:
        p = p + (k % b)
        p_counts = 0
print(counts_p)