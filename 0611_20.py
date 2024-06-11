a, b = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

# print(a, b)
# print(n)
# print(l)

for i in range(n):
    if l[i][0] < a:
        print("High")
    elif l[i][0] > a:
        print("Low")
    else:
        if l[i][1] > b:
            print("High")
        else:
            print("Low")