strs = list(input())
a, b = map(str, input().split())
a = int(a) - 1
strs[a] = b
for i in strs:
    print(i, end="")