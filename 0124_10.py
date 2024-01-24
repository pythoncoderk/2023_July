n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
# print(l)
final_sort = sorted(l, key=lambda x:(x[0], x[1], x[2]),reverse=True)
# print(final_sort)

for i in range(n):
    print(*final_sort[i])