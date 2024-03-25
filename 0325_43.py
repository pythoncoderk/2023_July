s = input()
x = s.index(":")

h_t = int(s[:x])
# print(h_t)

if h_t - 8 < 0:
    print(f"{h_t - 8 + 24}{s[x:]}")
else:
    print(f"{h_t - 8}{s[x:]}")