dane = [(3, 0), (4, 3), (0, 0), (2, 6), (0, 4)]
def czy_trojkat_prostokatny(dane):
    for i in range(len(dane)):
        for j in range(i + 1, len(dane)):
            for k in range(j + 1, len(dane)):
                # Sprawdzenie czy boki są równoległe do osi
                is_parallel = (dane[i][0] == dane[j][0] and dane[j][1] == dane[k][1]) or \
                              (dane[i][1] == dane[j][1] and dane[j][0] == dane[k][0]) or \
                              (dane[i][0] == dane[k][0] and dane[j][1] == dane[k][1])

                if is_parallel:
                    # Sprawdzanie czy długości boków spełniają warunek trójkąta prostokątnego
                    a = (dane[i][0] - dane[j][0])**2 + (dane[i][1] - dane[j][1])**2
                    b = (dane[i][0] - dane[k][0])**2 + (dane[i][1] - dane[k][1])**2
                    c = (dane[j][0] - dane[k][0])**2 + (dane[j][1] - dane[k][1])**2

                    sides = [a, b, c]
                    print(sides)
                    sides.sort()
                    print(sides)


                    if sides[2] == sides[0] + sides[1]:
                        # Sprawdzanie czy wewnątrz trójkąta nie ma innych punktów
                        is_inside = True
                        for p in dane:
                            if p != dane[i] and p != dane[j] and p != dane[k]:
                                det = (dane[i][0] - p[0]) * (dane[j][1] - dane[i][1]) - (dane[j][0] - dane[i][0]) * (dane[i][1] - p[1])
                                det2 = (dane[j][0] - p[0]) * (dane[k][1] - dane[j][1]) - (dane[k][0] - dane[j][0]) * (dane[j][1] - p[1])
                                det3 = (dane[k][0] - p[0]) * (dane[i][1] - dane[k][1]) - (dane[i][0] - dane[k][0]) * (dane[k][1] - p[1])
                                if (det >= 0 and det2 >= 0 and det3 >= 0) or (det <= 0 and det2 <= 0 and det3 <= 0):
                                    is_inside = False
                                    break
                        if is_inside:
                            return True
    return False
print(czy_trojkat_prostokatny(dane))