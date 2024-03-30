l = list(map(int, input().split()))
# print(l)

age = l[3] - l[2] * l[4]

# print(age)

if l[1] * l[-1] + age >= l[3]:
    print(l[3])
else:
    print(l[1] * l[-1] + age)
