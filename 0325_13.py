from datetime import datetime

n = int(input())

m = datetime(1, n, 1)
print(m.strftime("%B"))