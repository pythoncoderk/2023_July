n = int(input())
l = [list(map(str, input().split())) for i in range(n)]

# print(n)
# print(l)

for i in range(n):
    print("User{")
    print(f"nickname : {l[i][0]}")
    print(f"old : {l[i][1]}")
    print(f"birth : {l[i][2]}")
    print(f"state : {l[i][3]}")
    print("}")