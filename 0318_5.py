n = int(input())
l = [input() for i in range(n)]

# print(n)
# print(l)

g = 0
c = 0
p = 0

for i in range(n):
    if l[i] == "paper":
        p += 1
    elif l[i] == "scissors":
        c += 1
    else:
        g += 1

if g >= 1 and c >= 1 and p >= 1:
    print("draw")
elif g == 0 and c >= 1 and p >= 1:
    print("scissors")
elif g >= 1 and c == 0 and p >= 1:
    print("paper")
elif g >= 1 and c >= 1 and p == 0:
    print("rock")
elif g == n or c == n or p == n:
    print("draw")
