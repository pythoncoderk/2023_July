a, b, c, d = map(int, input().split())

x = int(not((int(not a) & int(not b)) | int(not c))) ^ d
print(x)