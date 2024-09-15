def calculate_minimum_coins_example():
    # 合計金額を入力として受け取る
    total_amount = int(input())  # 例として1234円を使用（必要に応じて変更可能）

    # 使用する硬貨の額面を降順でリスト化
    coins = [500, 100, 50, 10, 5, 1]

    # 各硬貨の枚数を格納する辞書
    coin_count = {500: 0, 100: 0, 50: 0, 10: 0, 5: 0, 1: 0}

    remaining_amount = total_amount

    # 最小の硬貨数を計算する
    for coin in coins:
        if remaining_amount >= coin:
            coin_count[coin] = remaining_amount // coin
            remaining_amount %= coin

    # 結果を表示する
    print(f"合計金額 {total_amount}円に対して最小の硬貨の組み合わせは:")
    for coin, count in coin_count.items():
        print(f"{coin}円硬貨: {count}枚")


# 実行例
calculate_minimum_coins_example()
