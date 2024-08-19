x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

l = []
l.append(x1)
l.append(x2)
l.append(x3)

l2 = []
l2.append(y1)
l2.append(y2)
l2.append(y3)

l_answer = [l.count(l[i]) for i in range(len(l))]
l2_answer = [l2.count(l2[i]) for i in range(len(l2))]

# print(l_answer)
# print(l2_answer)

l_answer_index = l_answer.index(1)
l2_answer_index = l2_answer.index(1)

print(l[l_answer_index], l2[l2_answer_index])