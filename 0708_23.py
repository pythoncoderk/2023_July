s = input().split("/")

# print(s)

x = int(s[0] + s[1] + s[2])

print("Heisei" if x <= 20190430 else "TBD")