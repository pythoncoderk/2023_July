n, m = map(int, input().split())
l = [str(input()) for i in range(n-2)]
l2 = [int(input()) for i in range(m)]

# print(n, m)
# print(l)
# print(l2)

total = 0
count = 0
for i in range(m):
    if total < n-1:
        total += l2[i]
        if l[i] == "+":
            total += 1
        elif l[i] == "-":
            total -= 1
        elif l[i] == "r":
            total = 0
    else:
        break
    count += 1
if total > n-1:
    total = n-1

# print(total)
# print(count)

goal = None
if total >= n - 1:
    goal = "goal"
else:
    goal = "still"

if goal == "goal":
    print(goal)
    print(count)
else:
    print(goal)
    print(total)