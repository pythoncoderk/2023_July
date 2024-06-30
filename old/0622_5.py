w, h = map(int, input().split())

if w % 16 == 0 and h % 9 == 0:
    x = "16:9"
else:
    x = "4:3"

print(x)