import sys
try:
    print("この段階では未だ例外は発生していない")

    print(sys.exc_info())
    sys.exit()

except:
    print("「現在」処理中の例外")
    print(sys.exc_info())

print("「現在」はもう例外処理中ではなくなった")
print(sys.exc_info())