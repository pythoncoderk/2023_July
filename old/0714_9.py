a, b, c, x = map(int, input().split())



if 1 <= x <= a:
    print(1)
elif a + 1 <= x <= b:
    y = b - a
    answer = c / y
    print(answer)
else:
    print(0)