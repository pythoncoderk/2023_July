s = input()

x = int(s[:2])
y = int(s[3:])

y += 30
if y >= 60:
    y -= 60
    x += 1
    if x >= 24:
        x -= 24

print(f"{str(x).zfill(2)}:{str(y).zfill(2)}")