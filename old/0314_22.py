l = list(map(str, input().split()))

# print(l)

days = int(l[0][-2:])
# print(days)

times = int(l[1][:2])
# print(times)

diff = times // 24
diff2 = times % 24

final_times = days + diff

print(f"{l[0][:3]}{final_times} {str(diff2).zfill(2)}{l[1][-3:]}")