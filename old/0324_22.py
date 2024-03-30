n = int(input())
s = input()

s_count = 0
r_count = 0

for i in range(n):
    if s[i] == "S":
        s_count += 1
    elif s[i] == "R":
        r_count += 1

print(f"{s_count} {r_count}")