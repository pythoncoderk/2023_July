a, b = map(int, input().split())

print("Yay!" if a <= 8 and b <= 8 and a + b <= 16 else ":(")