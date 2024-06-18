n = list(map(str, input().split()))

# print(n)

times = int(n[1][:2])
days = int(n[0][-2:])

# print(times)
# print(days)

x = times // 24
y = times % 24

days += x

mo = n[0][:3]

# print(mo)

mini = n[1][-3:]

# print(mini)

print(mo + str(days).zfill(2) + " " + str(y).zfill(2) + mini)