a, b = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    if l[i][0] == a:
        if l[i][1] < b:
            print("Low")
        else:
            print("High")
    elif l[i][0] < a:
        print("High")
    else:
        print("Low")