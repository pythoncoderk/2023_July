n = int(input())
l = list(input())

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z"]
for i in range(26):
    if i == 25:
        print(l.count(abc[i]))
    else:
        print(l.count(abc[i]), end=" ")