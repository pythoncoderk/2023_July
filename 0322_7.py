s, a, b = map(int, input().split())

# print(s, a, b)

bet = "A"
while True:
    if bet == "A":
        if s + 10 <= a:
            s += 10
            bet = "B"
        else:
            break
    else:
        if s + 1000 <= b:
            s += 1000
            bet = "A"
        else:
            break
if bet == "A":
    x = "B"
else:
    x = "A"

print(f"{x} {s}")