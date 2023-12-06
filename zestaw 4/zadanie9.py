import re

f = open("text.txt", "r")
text = f.read()

x = re.findall("[a-z()0-9][.?!] [A-Z]", text)
print(x)

count = len(x)
print('Liczba zdań to: ', count)