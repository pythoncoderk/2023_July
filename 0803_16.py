n = int(input())

if n % 4 != 0:
    print(365)
elif n % 4 == 0 and n % 100 != 0:
    print(366)
elif n % 100 == 0 and n % 400 != 0:
    print(365)
elif n % 400 == 0:
    print(366)