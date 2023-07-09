import time

print("Pythonを実行しています。")
print("実行を停止しました。")

for _ in range(10):
    print(".", end="")
    time.sleep(2)
print()
print("実行を再開します。")
print("完了しました。")

"""
### 実行結果 ###
Pythonを実行しています。
実行を停止しました。
..........
実行を再開します。
完了しました。
"""