s1 = {i for i in range(1, 11)}
print(s1)

# 出力結果 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

l = [1, 1, 1, 1, 1, 1]
s2 = {i for i in l}
print(s2)

# 出力結果 {1}

s3 = {i ** 2 for i in range(1, 11)}
print(s3)

# 出力結果 {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}