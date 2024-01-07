import sys

n = int(input())
s = input()

s_l = len(s)
if s_l >= n:
    s_one = s[n-1]
else:
    sys.exit()

if s_l >= n+1:
    s_two = s[n]
    print(s_one, s_two)
