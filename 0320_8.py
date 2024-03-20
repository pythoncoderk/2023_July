"""
深いコピー(deep copy)を作成
"""

l = [1, 2, 3, 4, 5]

deep_copy = l[:]

"""
そのまま出力
"""
print(f"l- {l}")
print(f"shallow_copy- {deep_copy}")
"""
出力結果
l- [1, 2, 3, 4, 5]
deep_copy- [1, 2, 3, 4, 5]
"""

"""
元になるlのインデックス0を10に更新
"""

l[0] = 10

print(f"l- {l}")
print(f"deep_copy- {deep_copy}")

"""
出力結果
l- [10, 2, 3, 4, 5]
deep_copy- [1, 2, 3, 4, 5]
"""