start = int(input('Podaj liczbę zaczynającą zakres '))
end = int(input('Podaj liczbę zaczynającą zakres '))
sum = 0
count =0 
for x in range(start,end+1):
    sum= sum + x
    count = count +1
if count <= 20:
    for x in range(start,end+1):
        print(x)
else:
    x = 4
    avg = sum /count
    while x > 1:
        x = x-1
        print(avg - x)
        
    while x < 4:
        print(avg + x)
        x = x+1

        
        