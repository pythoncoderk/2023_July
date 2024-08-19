s, a, b = map(int, input().split())

# print(s, a, b)

a_or_b = "a"
while True:
    if a_or_b == "a":
        if s + 10 <= a:
            s += 10
            a_or_b = "b"
        else:
            break
    else:
        if s + 1000 <= b:
            s += 1000
            a_or_b = "a"
        else:
            break

if a_or_b == "a":
    x = "B"
else:
    x = "A"

print(x, s)