import enum

class Sample(enum.Enum):
    MUSIC = enum.auto()
    BOOK = enum.auto()

print(Sample(2))