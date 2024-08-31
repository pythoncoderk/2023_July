f = open("test.txt", "w")
f.write("test\n")
print("I am print", file=f)
f.close()