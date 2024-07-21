k = int(input())

x = k // 60
y = k % 60

x_f = str(x + 21).zfill(2)
y_f = str(y).zfill(2)

print(f"{x_f}:{y_f}")