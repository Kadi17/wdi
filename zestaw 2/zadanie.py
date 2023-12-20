string = input('podaj ciąg znaków: ')
#print(len(string))
x = 0
evenN = 1
list = []
while x < len(string):
    if evenN % 2 == 0 and string[x] != '0':
        list.append(string[x])
    if string[x] == '0':
        evenN = evenN +1
    x = x+1
ascii = []
for letter in list:
    ascii.append((ord(letter)))
ascii.sort()
print(list)    
print(ascii)
print(ascii[4])