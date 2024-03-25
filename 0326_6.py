n = int(input())
l = list(map(str, input().split()))

# print(n)
# print(l)

g = l.count("G")
p = l.count("P")

if g == p:
    print("Draw")
elif g < p:
    print("G")
else:
    print("P")