s1 = input()
t1 = input()

l = ["AC", "CA", "DB", "BD", "EC", "CE", "AD", "DA", "BE", "EB"]
l2 = ["AB", "BA", "BC", "CB", "CD", "DC", "DE", "ED", "EA", "AE"]

s = 9
t = 9

if s1 in l:
    s = 1
elif s1 in l2:
    s = 2
if t1 in l:
    t = 1
elif t1 in l2:
    t = 2
if s == 1 and t == 1:
    print("Yes")
elif s == 2 and t == 2:
    print("Yes")
else:
    print("No")