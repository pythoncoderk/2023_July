s, a, b = map(int, input().split())

price = s
a1 = 0
b1 = 0
chk = "aa"
while True:
    if chk == "aa":
        price += 10
        chk = "bb"
        if price + 1000 > b:
            break
    else:
        price += 1000
        chk = "aa"
        if price + 10 > a:
            break

if chk == "aa":
    final = "B"
else:
    final = "A"

print(f"{final} {price}")