d = {"x": 10, "y": 20}
print(d)
print(d.keys())
print(d.values())
d2 = {"x": 1000, "j": 500}
d.update(d2)
print(d)
print(d["x"])
print(d.get("x"))
print(d.get("z"))
# print(d.pop("1000"))
print(d)
print(d.pop("x"))
print(d)