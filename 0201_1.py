n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
# print(n)
# print(l)

l2 = [l[i][0] + l[i][1] for i in range(n)]
# print(l2)
count_l = [l2.count(l2[i]) for i in range(n)]
# print(count_l)
max_l = max(count_l)

final_l = [l2[i] for i in range(n) if count_l[i] == max_l]
final_l.sort()
print(final_l[0])