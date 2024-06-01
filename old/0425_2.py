l = list(map(str, input().split()))

# print(l)

times = int(l[1][:2])
day_l = int(l[0][-2:])
# print(times)
# print(day_l)
days = 0

day_l += times // 24
times2 = times % 24

print(f"{l[0][:3]}{str(day_l + days).zfill(2)} {str(times2).zfill(2)}{l[1][-3:]}")