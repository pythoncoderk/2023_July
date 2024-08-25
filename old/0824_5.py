for i in range(0, 24):
    for j in range(0, 60):
        x = i + j
        if x % 3 == 0 and x % 5 == 0:
            print("FIZZBUZZ")
        elif x % 3 == 0:
            print("FIZZ")
        elif x % 5 == 0:
            print("BUZZ")
        else:
            print()
