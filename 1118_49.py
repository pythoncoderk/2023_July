import re

n = input()
if re.match(r"noaki", n) != None:
    print(re.sub("noaki", "", n))
else:
    print(n)