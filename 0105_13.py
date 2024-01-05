n = int(input())
l = [input() for i in range(n)]
for i in range(n):
    print(l[i].count("p") + l[i].count("a") + l[i].count("i") + l[i].count("z"))