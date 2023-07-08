def self_introduce(name, age, country, zoo):
    return "私は{}です。{}生まれでは{}歳です。{}にいます。".format(name, country, age, zoo)

print(self_introduce("らくだ", 32, "日本", "上野公園"))

def wrapped_introduce_limited(name, age):
    country = "日本"
    zoo = "上野公園"
    return self_introduce(name, age, country, zoo)

print(wrapped_introduce_limited("らくだ", 32))

def wrapped_introduce(args):
    return self_introduce(*args)

camel = ("らくだ", 32, "日本", "上野公園")
print(wrapped_introduce(camel))
