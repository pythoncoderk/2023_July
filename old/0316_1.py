h, w = map(int, input().split())
r, c = map(int, input().split())

l = [["X" for j in range(w)] for i in range(h)]

r1 = r-1
c1 = c-1

# print(h, w)
# print(r, c)
# print(l)

count = 0
if r1 - 1 >= 0:
    count += 1
if c1 - 1 >= 0:
    count += 1
if c1 + 1 <= w - 1:
    count += 1
if r1 + 1 <= h - 1:
    count += 1
print(count)