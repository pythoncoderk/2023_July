n, m = map(int, input().split())
l = []
for i in range(n-2):
    x1 = input()
    l.append(x1)

l2 = []
for i in range(m):
    x2 = int(input())
    l2.append(x2)

# print(n, m)
# print(l)
# print(l2)

count = 0
for i in range(m):
    count += l2[i]
    if count >= n-1:
        print("goal")
        print(i+1)
        exit()
    elif l[count-1] == "+":
        count += 1
    elif l[count-1] == "-":
        count -= 1
    elif l[count-1] == "r":
        count = 0
print("still")
print(count)
