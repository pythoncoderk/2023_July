import math

m, d = map(int, input().split())
p, n = map(int, input().split())

# print(m, d)
# print(p, n)

#割引対象数
down = n - (n // 4)
# print(down)

#通常価格数
n_price = n - down
# print(n_price)

#割引会計
down_buy = (down * p) - ((down * p) * d) * 0.01
down_buy = math.floor(down_buy)
# print(down_buy)

#通常会計
n_price_buy = n_price * p
# print(n_price_buy)

print(down_buy + n_price_buy)