import itertools
sorted_txt = "".join(sorted("aAhrBaahBBntSduKKlOaeavRdegadsSSQHMtdgda#"))
for i, j in itertools.groupby(sorted_txt):
    print(f"{i}: {list(j)}")

"""
### 出力内容 ###

#: ['#']
A: ['A']
B: ['B', 'B', 'B']
H: ['H']
K: ['K', 'K']
M: ['M']
O: ['O']
Q: ['Q']
R: ['R']
S: ['S', 'S', 'S']
a: ['a', 'a', 'a', 'a', 'a', 'a', 'a']
d: ['d', 'd', 'd', 'd', 'd']
e: ['e', 'e']
g: ['g', 'g']
h: ['h', 'h']
l: ['l']
n: ['n']
r: ['r']
s: ['s']
t: ['t', 't']
u: ['u']
v: ['v']

"""