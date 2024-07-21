n, m, x, t, d = map(int, input().split())

if m >= x:
    print(t)
else:
    answer = (x - m) * d
    print(t - answer)
