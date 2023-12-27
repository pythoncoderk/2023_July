times = input()

x = times.index(":")
hours = int(times[:x])
minutes = times[x:]

if hours - 5 < 0:
    hours = hours - 5 + 24
else:
    hours -= 5

print(str(hours) + minutes)