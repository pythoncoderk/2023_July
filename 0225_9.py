l = [6, 1, 7, 2, 8, 3, 9, 4, 10, 5]


def sort_l(arr):
    for i in range(len(arr)):
        for j in range(-1, i + (len(arr) * -1), -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

l_point = len(l) // 2
print(l_point)

x_l = l[:l_point]
y_l = l[l_point:]

x_l = sort_l(x_l)
y_l = sort_l(y_l)

print(x_l)
print(y_l)

final_l = []
while len(x_l) != 0 or len(y_l) != 0:
    if len(x_l) != 0 and len(y_l) != 0:
        if x_l[0] < y_l[0]:
            final_l.append(x_l.pop(0))
        else:
            final_l.append(y_l.pop(0))
    else:
        if len(x_l) == 0:
            final_l.append(y_l.pop(0))
        else:
            final_l.append(x_l.pop(0))

print(final_l)
