a, b = map(int, input().split())

print("Yes" if a + 1 == b or a - 1 == b or (a == 1 and b == 10) or (a == 10 and b == 1) else "No")
