l = [["akira", 24], ["masako", 18], ["jun", 33], ["yoshio", 15]]
l_sort = sorted(l, key=lambda x: x[1], reverse=True)
for _ in range(len(l)):
    print(*l_sort[_])

# 出力結果
"""
jun 33
akira 24
masako 18
yoshio 15
"""