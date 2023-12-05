n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
# print(n)
# print(l)
def names(x):
    print("User{")
    print(f"nickname : {x[0]}")
    print(f"old : {x[1]}")
    print(f"birth : {x[2]}")
    print(f"state : {x[3]}")
    print("}")
for i in range(n):
    x = l[i]
    names(x)