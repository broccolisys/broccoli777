import re
import random
# p = re.compile('[a-z]*')
# m = p.match("python")
# print(m)

# p = re.compile(r"(?P<greeting>\w+)\s\1")
# m = p.search("sdf Hello Hello")
# print(m)
# print(m.group("greeting"))
#
# s = re.compile(r"(\w+)\s(\w+)\s\1\s\2")
# c = s.search("sdf Hello World Hello World dkfjdksj ")
# print(c)
#
# print(3 != 4)
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

s = re.compile(".+(?=:)")
g = s.search("http://google.com")
print(g.group())
