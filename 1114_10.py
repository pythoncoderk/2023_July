import re

s = input()
print(re.search(r"Math[123][ABC]", s).start())

s = input()
print(re.search(r"Math[123][ABC]", s).start())