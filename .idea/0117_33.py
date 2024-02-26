import re

n = int(input())
l = [input() for i in range(n)]

for i in l:
    x = re.fullmatch(r"([1][\d]{,1}|[2][0-5]{,1}|[\d]{,1})(\.[1][\d]{,1}|[2][0-5]{,1}|[\d]{,1}){2}", i)
    print(x)