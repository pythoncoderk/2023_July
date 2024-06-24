l = list(map(int, input().split()))
l.sort()

max_l = l[-1]
max_l_2 = l[-2]

answer = str(max_l) + str(max_l_2)
answer_2 = int(answer)

print(answer_2 + l[0])
