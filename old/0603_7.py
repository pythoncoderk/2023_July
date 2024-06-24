a, b, c = map(int, input().split())

# print(a, b, c)

if c == 0:
    a -= 1
else:
    b -= 1

print("Takahashi" if a >= b else "Aoki")