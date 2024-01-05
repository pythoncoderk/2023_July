from decimal import Decimal, ROUND_HALF_UP

# 小数点第一位を四捨五入
print(Decimal(str(0.1)).quantize(Decimal("0"), ROUND_HALF_UP))
# 出力結果 0

print(Decimal(str(0.4)).quantize(Decimal("0"), ROUND_HALF_UP))
# 出力結果 0

print(Decimal(str(0.5)).quantize(Decimal("0"), ROUND_HALF_UP))
# 出力結果 1

# 小数点第二位を四捨五入
print(Decimal(str(0.01)).quantize(Decimal("0.1"), ROUND_HALF_UP))
# 出力結果 0.0

# 小数点第二位を四捨五入
print(Decimal(str(0.05)).quantize(Decimal("0.1"), ROUND_HALF_UP))
# 出力結果 0.1

# 小数点第三位を四捨五入
print(Decimal(str(0.001)).quantize(Decimal("0.01"), ROUND_HALF_UP))
# 出力結果 0.00

# 小数点第三位を四捨五入
print(Decimal(str(0.005)).quantize(Decimal("0.01"), ROUND_HALF_UP))
# 出力結果 0.01

