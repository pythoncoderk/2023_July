h, w = map(int, input().split())
if h % 2 == 0 and w % 2 == 0 and h != 0 and w != 0:
    print("YES")
else:
    print("NO")