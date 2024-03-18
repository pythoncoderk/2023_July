s = list(map(str, input().split()))
x = int(s[1][:2])
z = int(s[0][-2:])
# print(s)
# print(x)
# print(z)

count = 0
while x >= 24:
    x -= 24
    count += 1
print(f"{s[0][:3]}{str(z + count).zfill(2)} {str(x).zfill(2)}{s[1][-3:]}")
