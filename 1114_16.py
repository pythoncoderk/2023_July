import re

n = input()
print(re.search(r"CVE-[0-9]{4}-[0-9]*", n).start())