a, b = map(str, input().split())

count_a = 0
if len(a) > len(b):
    count_a = len(a)
elif len(a) < len(b):
    count_a = len(b)
else:
    count_a = len(a)

a = list(str(a).zfill(count_a))
b = list(str(b).zfill(count_a))

final_l = []
for i in range(count_a):
    final_l.append(str(int(a[i]) + int(b[i]))[-1])
for i in range(count_a):
    print(final_l[i], end="")