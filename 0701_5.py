import re
l = "1234567891"
x = re.split("(...)", l)[1::2]
print(",".join(x))

