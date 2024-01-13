
l = [6, 5, 4, 3, 1, 2,]
"""
選択ソートの実装
①　配列の最小値を探す
②　最小値を配列の先頭に移動する
③　①～②の処理で先頭はソート完了と考えて①～②を繰り返す
"""
counts = 0
for i in range(len(l)):
    min_l = l[i]
    for j in range(i, len(l)):
        if min_l > l[j]:
            min_l = l[j]
    for i in range(len(l)):
        if l[i] == min_l:
            l.pop(i)
            l.insert(counts, min_l)
    counts += 1
print(l)