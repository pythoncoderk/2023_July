n = input()

x = n[-1]

hon = ["2", "4", "5", "7", "9"]
pon = ["0", "1", "6", "8"]
bon = ["3"]

if x in hon:
    print("hon")
elif x in pon:
    print("pon")
else:
    print("bon")