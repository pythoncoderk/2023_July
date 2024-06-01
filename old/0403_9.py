s = input()

# print(s)

index_s = s.index("SUNSET") + 6
# print(index_s)

sun = s[index_s:index_s+3]
# print(sun)

sun_len = len(sun)

if sun_len < 3:
    for i in range(3 - sun_len):
        sun += s[i]

print(sun)