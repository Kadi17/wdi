high = int(input('Podaj wysokość choinki'))
base = ''
space = high -1
add = 0 
for x in range (1, high+1):
    base =  space * " " +(x+add) * '*'
    print(base)
    add = add +1
    space = space -1