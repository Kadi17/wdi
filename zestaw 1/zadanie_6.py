numberOne = int(input('Podaj pierwszą liczbę '))
numberTwo = int(input('Podaj drugą liczbę '))


if numberOne < 0 and numberTwo <0:
    print('Koniec programu nie może być dwóch liczb mniejszych niż zero')
    exit(1)
elif numberOne < 0 and numberTwo >= 0:
    numberOne = numberOne * -1
elif numberTwo < 0 and numberOne >= 0:
    numberTwo = numberTwo * -1


#Suma
sum = numberOne + numberTwo
print("Wynik z dodawania to:", sum)
#Róźnica
difference = numberOne - numberTwo
print("Wynik z odejmowania to:", difference)

#Iloczyn
multiple = numberTwo * numberOne
print("Wynik z mnożenia to:", multiple)

"""
Sprawdzenie czy liczba jest podzielna przez 10
"""
if multiple%10 == 0:
    print('Yay!')

#Iloraz
quotient = numberOne / numberTwo
print("Wynik z dzielenia to:", quotient)

square1 = numberOne **2
print("Kwadrat pierwszej liczby to:", square1)

square2 = numberTwo **2
print("Kwadrat drugiej liczby to:", square2)

sqrt1 = numberOne ** 0.5
print("Pierwiastek pierwszej liczby to:", sqrt1)

sqrt2 = numberTwo ** 0.5
print("Pierwiastek drugiej liczby to:", sqrt2)


