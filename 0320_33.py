n = int(input())

l = [input() for i in range(n)]

# print(l)

r = l.count("rock")
s = l.count("scissors")
p = l.count("paper")

if r >= 1 and s >= 1 and p >= 1:
    print("draw")
elif (r == 0 and s == 0) or (s == 0 and p == 0) or (r == 0 and p == 0):
    print("draw")
elif r == 0:
    print("scissors")
elif s == 0:
    print("paper")
elif p == 0:
    print("rock")




