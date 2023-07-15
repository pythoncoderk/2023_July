import itertools
it = itertools.chain(["A", "B", "C"], "xyx", range(5))
for i in it:
    print(i)

"""
### 出力内容 ###

A
B
C
x
y
x
0
1
2
3
4

"""