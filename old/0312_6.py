n = int(input())
s = input()

fast = 0
last = 0

for i in range(len(s)):
    if s[i] == "|":
        fast = i
        break

for i in range(len(s)-1, -1, -1):
    if s[i] == "|":
        last = i
        break

# print(fast)
# print(last)

# print(s[fast:last+1])

s2 = s[fast:last+1]

count = 0
for i in range(len(s2)):
    if s2[i] == "*":
        count += 1

if count >= 1:
    print("in")
else:
    print("out")