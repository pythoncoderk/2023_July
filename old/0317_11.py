l = [list(input()) for i in range(2)]

if (l[0] == ["#", "."] and l[1] == [".", "#"]) or (l[1] == ["#", "."] and l[0] == [".", "#"]):
    print("No")
else:
    print("Yes")