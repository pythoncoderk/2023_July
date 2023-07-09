def generator():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x
g = generator()

print("next 1 回目")
next(g)
print("next 2 回目")
next(g)
print("next 3 回目")
next(g)

"""
### 出力内容 ###

next 1 回目
next 2 回目
next 3 回目

"""
