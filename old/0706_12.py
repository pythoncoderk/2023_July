a = int(input())
b = int(input())
c = int(input())


while True:
    if c % a == 0 and c % b == 0:
        print(c)
        exit()
    else:
        c += 1