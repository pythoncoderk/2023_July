n = int(input())
l = list(map(str, input().split()))

# print(n)
# print(l)

zero = 0
ten = 0
for i in range(n):
    if l[i] == "0":
        zero += 1
        l[i] = int(l[i])
    elif l[i] == "x10":
        ten += 1
        l[i] = 0
    else:
        l[i] = int(l[i])

# print(l)

max_l = max(l)

if zero >= 1:
    l.append(max_l * -1)

print(sum(l) * 10 if ten >= 1 else sum(l))