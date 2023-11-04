x = list(input())
if x[0] == "A":
    x[0] = "R"
for i in range(len(x)):
    if i == len(x) - 1:
        print(x[i])
    else:
        print(x[i], end="")