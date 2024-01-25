a, b = map(int, input().split())
counts = 0
while a != 0 or b != 0:
    a -= 1
    b -= 1
    counts += 1
