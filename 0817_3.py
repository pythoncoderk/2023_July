h, w = map(int, input().split())

print("YES" if h % 2 == 0 and h != 0
        and w != 0 and w % 2 == 0 else "NO")