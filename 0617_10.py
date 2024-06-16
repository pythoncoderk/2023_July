x, y = map(int, input().split())

a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]

x_answer = ""
y_answer = ""

if x in a:
    x_answer = "a"
elif x in b:
    x_answer = "b"
else:
    x_answer = "c"

if y in a:
    y_answer = "a"
elif y in b:
    y_answer = "b"
else:
    y_answer = "c"

print("Yes" if x_answer == y_answer else "No")