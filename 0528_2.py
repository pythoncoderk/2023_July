import heapq

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(n)
# print(l)

heapq_l = []
for i in range(n):
    if l[i][0] == 1:
        heapq.heappush(heapq_l, l[i][1])
    elif l[i][0] == 2:
        print(min(heapq_l))
    else:
        heapq.heappop(heapq_l)