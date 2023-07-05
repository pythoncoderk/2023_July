try:
    num1 = 5 / 0
    num2 = 5 / "0"

except ZeroDivisionError:
    print("ZeroDivisionError")

except TypeError:
    print("TypeError")