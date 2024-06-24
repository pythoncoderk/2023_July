n, k = map(int, input().split())

l = [0] * k


def test(x, y, arr):
    count = 0
    for i in range(y):
        x -= 1
        if x < 0:
            break
        else:
            arr[count] += 1
            count += 1
    return x, y, arr


while n > 0:
    n, k, l = test(n, k, l)

l_max = max(l)
l_min = min(l)

print(l_max - l_min)