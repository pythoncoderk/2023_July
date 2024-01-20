n = int(input())
final = n

counts = 0
while n > 26:
    n -= 26
    counts += 1

counts2 = 0
if counts > 26:
    while counts > 26:
        counts -= 26
        counts2 += 1
# print(counts2)
# print(counts)
# print(n)

if final <= 26:
    print(chr(n+64))
elif counts2 == 0:
    print(f"{chr(counts+64)}{chr(n+64)}")
else:
    print(f"{chr(counts2+64)}{chr(counts+64)}{chr(n+64)}")