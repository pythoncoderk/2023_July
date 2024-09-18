h = int(input())

pai = []
mon = []
now = "p"
pai_count = 0
mon_count = 0
while True:
    if now == "p":
        pai_count += 1
        if pai_count == 1 or pai_count == 2:
            mon.append(1)
        else:
            mon.append(pai[-1] + pai[-2])
    else:
        mon_count += 1
        if mon_count == 1 or mon_count == 2:
            pai.append(1)
        else:
            pai.append(mon[-2] * 2 + mon[-3])
    if sum(pai) >= h:
        print(mon_count)
        break
    if now == "p":
        now = "m"
    else:
        now = "p"

