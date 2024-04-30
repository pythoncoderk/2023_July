a, b = map(str, input().split())

a = list(a)
b = list(b)

# print(a)
# print(b)

a_len = len(a)
b_len = len(b)

if a_len > b_len:
    for i in range(a_len - b_len):
        b.insert(0, 0)
elif a_len < b_len:
    for i in range(b_len - a_len):
        a.insert(0, 0)

# print(a)
# print(b)

a_l = [int(a[i]) for i in range(len(a))]
b_l = [int(b[i]) for i in range(len(b))]

# print(a_l)
# print(b_l)

max_len = 0
if len(a_l) > len(b_l):
    max_len = len(a_l)
else:
    max_len = len(b_l)

total = ""
for i in range(max_len):
    x = a_l[i] + b_l[i]
    x = str(x)[-1]
    total += x

print(total)