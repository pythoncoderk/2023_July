n = int(input())
l = [int(input()) for i in range(n)]

# print(n)
# print(l)

def get_m(x):
    y = 1
    count = 0
    while x != y:
        if x % y == 0:
            count += y
            y += 1
        else:
            y += 1
    return count


for i in range(n):
    if get_m(l[i]) == l[i]:
        print("perfect")
    elif get_m(l[i]) == l[i] - 1 or get_m(l[i]) == l[i] + 1:
        print("nearly")
    else:
        print("neither")