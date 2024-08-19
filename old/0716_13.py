l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

s = list(map(int, input()))

set_l = set(l)
set_s = set(s)

x = set_l - set_s

print(*x)