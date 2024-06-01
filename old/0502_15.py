n, a, b = map(int, input().split())

# print(n, a, b)

n_l = list(input())
a_l = list(input())
b_l = list(input())

# print(n_l)
# print(a_l)
# print(b_l)

for i in range(n):
    x = n_l.pop(0)
    if a_l:
        if x == a_l[0]:
            a_l.pop(0)
    if b_l:
        if x == b_l[0]:
            b_l.pop(0)

print(len(a_l), len(b_l))


