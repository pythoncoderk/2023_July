x, y = map(str, input().split())

# print(x, y)

x_l = list(x)
y_l = list(y)

x_l2 = [int(x_l[i]) for i in range(len(x_l))]
y_l2 = [int(y_l[i]) for i in range(len(y_l))]

x_sum = str(sum(x_l2))[-1]
y_sum = str(sum(y_l2))[-1]

if x_sum == y_sum:
    print("Draw")
elif x_sum < y_sum:
    print("Alice")
else:
    print("Bob")