l = int(input())
u, a, b = map(int, input().split())
v = int(input())

# print(l)
# print(u, a, b)
# print(v)

km = 0
kame = 0
usa = 0
while km != l:
    km += 1
    kame += v
    usa += u
    if l == km:
        break
    elif km % a == 0:
        usa += b

if kame == usa:
    print("DRAW")
elif kame < usa:
    print("KAME")
else:
    print("USAGI")