n = int(input())
l = [input() for i in range(n)]
for i in l:
    if i == "forward":
        print("Sunny")
    elif i == "reverse":
        print("Rainy")
    elif i == "sideways":
        print("Cloudy")