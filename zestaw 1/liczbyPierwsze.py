number = input("Podaj liczbę ")
x = 0
if int(number) == 1  or int(number) == 0:
    print('nie jest liczbą pierwszą')
else:
    for i in range(2, int(number)):
        if int(number) % i == 0:
            x = x+1
    if x == 0:
        print('jest liczbą pierwszą')
    else:
        print('nie jest')