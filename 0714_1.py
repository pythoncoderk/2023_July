name: str = "名前" # 変数名前をstr型と宣言

def f(arg: int) -> str: # 引数argはint型で受取り、戻り値はstr型
    return str(arg)

print(f("テスト"))