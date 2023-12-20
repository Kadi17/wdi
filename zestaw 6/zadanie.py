def podzialy(liczba, skladniki, aktualny_podzial, start=1):
    if liczba == 0:
        print(aktualny_podzial)
        return
    for i in range(start, liczba + 1):
        print(i)
        skladniki.append(i)
        print(skladniki)
        podzialy(liczba - i, skladniki, aktualny_podzial + f"{i} + ", i)
        skladniki.pop()

# Przykład użycia:
liczba = 3
print(f"Wszystkie podziały liczby {liczba} na sumę składników:")
podzialy(liczba, [], "")
