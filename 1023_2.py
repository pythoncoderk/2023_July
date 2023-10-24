for i in range(24):
    for j in range(60):
        if (i + j) % 15 == 0:
            print("FIZZBUZZ")
        elif (i + j) % 3 == 0:
            print("FIZZ")
        elif (i + j) % 5 == 0:
            print("BUZZ")
        else:
            print()
