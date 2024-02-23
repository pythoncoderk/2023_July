n, m = map(int, input().split())
l = [input() for i in range(m)]

# print(l)

ok_list = [l[i] for i in range(m-n)]
# print(ok_list)

ng_list = [l[i] for i in range(-1, (n * -1)-1, -1)]
# print(ng_list)

final_list = [i for i in ok_list if i not in ng_list]
print(len(set(final_list)))