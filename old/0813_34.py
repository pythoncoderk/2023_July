a, b, n = map(int, input().split())
l = list(map(int, input().split()))

for i in l:
    if i == a:
        print(b)
    elif i == b:
        print(a)
    else:
        print(i)