n = int(input())
l = list(map(str, input().split()))
g = l.count("G")
p = l.count("P")
if g < p:
    print("G")
elif g == p:
    print("Draw")
else:
    print("P")