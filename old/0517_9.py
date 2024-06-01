n = 4
l = [5, 8, 9, 20]
s = 20

count_bin = False
bin_x = ""
i = 0
while bin_x != "1" * n:
    x = bin(i)
    bin_x = x[2:].zfill(n)
    i += 1
    total = 0
    for ii in range(n):
        if bin_x[ii] == "1":
            total += l[ii]
    if total == s:
        count_bin = True

if count_bin:
    print("Yes")
else:
    print("No")