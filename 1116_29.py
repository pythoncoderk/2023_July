import re

# m = re.match("a.c", "abc")
# print(m.group())

# m = re.search("a.c", "test abc test abc")
# print(m)
# print(m.span())
# print(m.group())

# m = re.findall("a.c", "test abc test abc")
# print(m)

# m =re.finditer("a.c", "test abc test abc")
# print(m)
# print([w.group() for w in m])

# m = re.match("a{2,4}", "aaaaaaa")
# print(m)

# m = re.match("[a-zA-Z0-9_]", "_")
# print(m)

# m = re.match("\W", "@")
# print(m)

# m = re.match("\D", "1")
# print(m)


# m = re.match("a|b", "b")
# print(m)

# x = "0.0.0.0"
# m = re.match(("([1-2][0-9][0-9]\.|[0-9][0-9]\.|[0-9]\.)([1-2][0-9][0-9]\.|[0-9][0-9]\.|[0-9]\.)"
#               "([1-2][0-9][0-9]\.|[0-9][0-9]\.|[0-9]\.)([1-2][0-9][0-9]\.|[0-9][0-9]\.|[0-9])", x))
# print(m)

# m = re.match("\S", " ")
# print(m)

# m = re.match("\?", "?")
# print(m)


# m = re.search("abc$", "tabcdtestabct")
# print(m)


s = ("https://cdnjs.cloudflare.com/ajax/libs/"
     "highlight.js/11.7.0/styles/atom-one-light.min.css")
print(s)


