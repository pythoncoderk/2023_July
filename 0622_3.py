a, b, c = map(int, input().split())


def loops(x, y):
    count = 0
    while x <= y:
        y -= x
        count += 1
    return count


x = loops(a, c)
y = loops(b, c)

print(x if x > y else y)