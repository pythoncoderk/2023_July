s = "my name is mike. hi mike."
print(s)
is_start = s.startswith("my")
print(is_start)

is_start = s.startswith("o")
print(is_start)

print(s.find("mike"))
print(s.rfind("mike"))
print(s.count("mike"))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace("mike", "Nancy"))