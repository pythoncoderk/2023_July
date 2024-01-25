s, a, b = map(int, input().split())
# print(s, a, b)

if a > b:
    max_price = a
else:
    max_price = b
ent = "a"
while s < max_price:
    if ent == "a":
        if s + 10 <= a:
            s += 10
            ent = "b"
        else:
            ent = "B"
            break
    else:
        if s + 1000 <= b:
            s += 1000
            ent = "a"
        else:
            ent = "A"
            break
print(f"{ent} {s}")