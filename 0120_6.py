import re
n = int(input())
l = [input() for i in range(n)]

for i in range(n):

    x = re.fullmatch(r"((2[0-5]{,2}|1\d{2}|\d{1,2})\.)"
                r"{3}(2[0-5]{,2}|1\d{2}|\d{1,2})", l[i])
# 0.0.0.0 ～ 255.255.255.255 の範囲内であれば True
# 範囲外であれば　Falseを返す
    if x is None:
        print(False)
    else:
        print(True)

# 出力結果 True