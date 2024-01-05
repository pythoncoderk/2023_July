a, b, c = map(int, input().split())
if c >= 20:
    b *= 4
elif c >= 15 and c <= 19:
    b *= 3
elif c >= 10 and c <= 14:
    b *= 2
elif c >= 5 and c <= 9:
    b = b
else:
    b = 0
print(a + b)