x = "MUSIC book".swapcase()
print(x)
# swapcase は大文字を小文字に、小文字を大文字に変換する


y = "music book".title()
print(y)
# 単語ごとに大文字1文字 + 小文字の形に変換する

z = "music book".capitalize()
print(z)
# 先頭1文字を大文字に、それ以外を小文字に変換する

import unicodedata

aa = unicodedata.normalize("NFKC", "ｱアＡA")
print(aa)


