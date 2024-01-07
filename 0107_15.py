"""
 1 ～ 10 までの数値で奇数であれば odd 偶数であれば even を
 リストに格納する
"""
# 空のリストを作成して、for loopで回した後に格納するパターン
l = []
for i in range(1, 11):
    if i % 2 == 0:
        l.append("even")
    else:
        l.append("odd")
print(*l)
# 出力結果 even odd even odd even odd even odd even odd

# リスト内包表記で書くパターン
l = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]
print(*l)
# 出力結果 even odd even odd even odd even odd even odd
