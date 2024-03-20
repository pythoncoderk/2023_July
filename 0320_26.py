t = list(map(str, input().split()))

# print(t)

x = int(t[1][:2])
# print(x)

count = 0
while x >= 24:
    count += 1
    x -= 24

days = int(t[0][-2:])
days += count

print(f"{t[0][:3]}{days} {str(x).zfill(2)}{t[1][-3:]}")

