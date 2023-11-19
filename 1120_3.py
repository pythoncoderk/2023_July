n = input()
x = n.find(":")
t1 = int(n[:x])
t2 = n[x+1:]
if t1 - 8 < 0:
    t1 = 24 - (8 - t1)
else:
    t1 = t1 - 8
print(f"{t1}:{t2}")
