import re

#str="906625611@qq.com"
#regex = re.compile("r'^[0-9-zA-Z]{0,}@[0-9-zA-Z]{0,}\.[0-9-zA-Z]{0,}'$")
#print(regex.match(str))

str="13911436525"
regex = re.compile(r'^\d{1}\d{10}$')
print(regex.match(str))
print(re.match(regex,str))


