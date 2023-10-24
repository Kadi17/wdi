import random
continu = 'T'
while continu == 'T' or continu =='t':
    firstNumber = int(input('Podaj liczbę pierwszą: '))
    secondNumber = int(input('Podaj liczbę drugą: '))
    operation = input('Wybierz typ operacji: \n + dodawanie \n - odejmowanie \n * mnożenie \n / dzielenie \n # potęgowanie \n ^ pierwiastkowanie \n x losowanie liczby z zakresu\n')
    match operation:
        case "+":
            print(firstNumber + secondNumber)
        case "-":
            print(firstNumber - secondNumber)
        case "*":
            print(firstNumber * secondNumber)
        case "/":
            print(firstNumber / secondNumber)
        case "#":
            print(firstNumber ** secondNumber)
        case "^":
            print(firstNumber ** (1/secondNumber))
        case "x":
            print(random.randint(firstNumber, secondNumber))
    continu = input("Czy chcesz wprowadzić nowe dane? T/N ")
    