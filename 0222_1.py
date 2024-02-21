l = [20, 2, 5, 1, 4, 6, 3, 7, 9, 8, 10, 11, 19, 18, 16, 17, 15, 14, 13, 12]
print(l)
# 出力結果
# [20, 2, 5, 1, 4, 6, 3, 7, 9, 8, 10, 11, 19, 18, 16, 17, 15, 14, 13, 12]

def sort_l(x):
    for i in range(len(x)):
        min_l = x[i]
        top, top_i = x[i], x.index(x[i])
        for j in range(i+1, len(x)):
            if min_l > x[j]:
                min_l, min_l_i = x[j], x.index(x[j])
        if min_l != top:
            x[top_i], x[min_l_i] = x[min_l_i], x[top_i]
    return x

print(sort_l(l))
# 出力結果
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


