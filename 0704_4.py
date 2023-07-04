def multiplier(values):
    ret = []
    for i in values:
        ret.append(2 ** i)
    return ret

values = [0, 1, 2, 3, 4, 5]
ret = multiplier(values)
print(type(ret))
print(ret)