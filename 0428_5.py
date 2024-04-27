n, a, b = map(int, input().split())

# print(n, a, b)

bet = "A"
while True:
    if bet == "A":
        if n + 10 <= a:
            n += 10
            bet = "B"
        else:
            bet = "B"
            break
    else:
        if n + 1000 <= b:
            n += 1000
            bet = "A"
        else:
            bet = "A"
            break
print(bet, n)
