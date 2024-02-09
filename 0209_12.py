h, w = map(int, input().split())
l = [list(map(int, input().split())) for i in range(h)]
r, c = map(int, input().split())
l2 = [list(input()) for i in range(r)]
print(h, w)
print(l)
print(r, c)
print(l2)
for k in range(w-c+1):
    for i in range(r):
        for j in range(w-c+1):
            print(f"{k}{j}", end=" ")
        print()