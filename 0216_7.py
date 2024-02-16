n, m = map(int, input().split())
l = [input() for i in range(m)]
l2 = [int(input()) for i in range(m)]

# print(n, m)
# print(l)
# print(l2)
run = 0
count = 0
goal = False
for i in range(m):
    count += 1
    run += l2[i]
    if l[i] == "-":
        run -= 1
    elif l[i] == "+":
        run += 1
    elif l[i] == "r":
        run = 0
    if run >= n:
        print("goal")
        print(count)
        goal = True
        break
if not goal:
    print("still")
    print(run)
