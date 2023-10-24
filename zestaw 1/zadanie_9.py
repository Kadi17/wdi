print("Witamy w usługach bankowych")
balans = 0
while exit != 4:
    options = int(input('Jaką operacje wbierasz:\n 1 - Wpłata \n 2 - Wypłata\n 3 - Sprawdź saldo \n 4 - Wyjście z banku '))
    pin = 0
    if options == 4:
        print('Zapraszamy ponownie')
        exit = 4
        break
    while pin != 1234:
        pin = int(input('Podaj pin: '))
        if pin == 1234:
            if options == 1:
                pay = int(input('Podaj kwotę '))
                balans = balans + pay
            elif options == 2:
                withdraw = int(input('Podaj kwotę '))
                balans = balans - withdraw
            elif options == 3:
                print('Na koncie posiadasz: ', balans, "\n")
            else:
                print('Nie ma takiej opcji')
        else:
            print('Błędny pin')
        


