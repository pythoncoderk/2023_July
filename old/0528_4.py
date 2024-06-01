n = int(input())
l = [int(input()) for i in range(n)]
Map = {}

print(n)
print(l)

answer = 0
for a in l:
    answer += Map.get(a, 0)
    Map[a] = Map.get(a, 0) + 1

print(answer)