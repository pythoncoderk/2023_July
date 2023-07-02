import re
s = "バナナは$0000です"
m = re.search(r"\$[0-9]+",s)
print(m)
if m:
    print(m.group())
    print(m.span())