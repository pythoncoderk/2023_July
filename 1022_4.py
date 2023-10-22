n = int(input())
l = [i+1 for i in range(n)]
x = l.pop(0)
while len(l) != 1:
    x = x * l.pop(0)
x = x * l[0]

point = list(str(x))

counts = []
while point[-1] == "0":
    counts.append(point.pop(-1))
print(len(counts))