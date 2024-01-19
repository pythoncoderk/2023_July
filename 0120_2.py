# n と k を取得
n, k = map(int, input().split())

# a_1, a_2 ... a_n を取得
input_list = input().split()
a_list = list(map(int, input_list))

# キャンペーンの各区間の平均値
average = []
# for i in range(n - k + 1):
#     i_average = 0
#     for j in range(k):  # k日間分足して平均を求める
#         i_average += a_list[i + j]
#
#     average.append(i_average / k)
sum_day = []
tmp = 0
for i in range(k):
    tmp += a_list[i]
sum_day.append(tmp)
for i in range(n-k):
    tmp -= a_list[i]
    tmp += a_list[i+k]
    sum_day.append(tmp)
# print(sum_day)
max_l = max(sum_day)
count_l = sum_day.count(max_l)
index_l = sum_day.index(max_l)

print(f"{count_l} {index_l+1}")





