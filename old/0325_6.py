a, b = map(int, input().split())

if len(str(a * b)) >= 5:
    print("NG")
else:
    print(a * b)