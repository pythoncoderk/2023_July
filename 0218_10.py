l = [1, 2, 3, 4, 5]
# 1 x 2 x 3 x 4 x 5 なので総乗は 120となる
prod_total = 1
for _ in range(len(l)):
    prod_total *= l[_]
print(prod_total)

# 出力結果
120