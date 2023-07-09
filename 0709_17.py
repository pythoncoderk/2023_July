import itertools
for v in itertools.zip_longest("abcde", "123", "あいうえ", fillvalue="-"):
    print(v)