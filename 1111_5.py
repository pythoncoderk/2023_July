n = int(input())
l = [i+1 for i in range(n)]
for _ in l:
    if _ % 15 == 0 and _ != 0:
        print("Fizz Buzz")
    elif _ % 3 == 0 and _ != 0:
        print("Fizz")
    elif _ % 5 == 0 and _ != 0:
        print("Buzz")
    else:
        print(_)