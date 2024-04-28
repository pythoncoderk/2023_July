def calculate_score(cards):
    # 2枚のカードをそれぞれ2桁の整数とみなし、和を計算する
    left = cards[0] * 10 + cards[1]
    right = cards[2] * 10 + cards[3]
    return left + right

def max_score(cards):
    max_score = 0
    # 4枚のカードの全ての順序を試す
    for a in range(4):
        for b in range(4):
            if b != a:
                for c in range(4):
                    if c != a and c != b:
                        d = 6 - a - b - c  # 4枚のうち残りのカード
                        score = calculate_score([cards[a], cards[b], cards[c], cards[d]])
                        if score > max_score:
                            max_score = score
    return max_score

# カードの数字
cards = [2, 9, 3, 8]

# 最大スコアを計算
print(max_score(cards))
