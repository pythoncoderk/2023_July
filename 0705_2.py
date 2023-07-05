from dataclasses import dataclass
@dataclasses
class User:
    name: str
    age: int

user = User("sato", 20)
print(user.name)
print(user.age)