d, t = map(str, input().split())
day = int(d[-2:])
times = int(t[:2])
# print(times)

f_day = d[:2]
f_times = t[-2:]
final_time1 = int(times) // 24
final_time2 = int(times) % 24
# print(final_time1)

day += final_time1

# print(day)
# print(final_time1)
# print(final_time2)
print(f"{f_day}/{str(day).zfill(2)} {str(final_time2).zfill(2)}:{f_times}")