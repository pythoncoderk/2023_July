import math

m, d = map(int, input().split())
p, n = map(int, input().split())
# print(f"m {m} 割引対象数")
# print(f"d {d} 割引率%")
# print(f"p {p} 通常価格")
# print(f"n {n} 購入数")
#割引購入数
price_down = (n // m) * m
# print(price_down)
price_down_buy = price_down * p - (((price_down * p) * d) * 0.01)
# print(price_down_buy)
#通常購入数
price = n - price_down
price_buy = price * p
# print(price_buy)
print(math.floor(price_buy + price_down_buy))


