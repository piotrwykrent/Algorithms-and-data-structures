def binary_search(lista, cel):
    lewy = 0
    prawy = len(lista) - 1
    while lewy <= prawy:
        srodek = (lewy + prawy) // 2
        if lista[srodek] == cel:
            return srodek
        elif lista[srodek] < cel:
            lewy = srodek + 1
        else:
            prawy = srodek - 1
    return -1


# Przykład użycia:
moja_lista = [0, 1, 1, 2, 3, 6, 6, 7, 8]  # Musi być posortowana!
szukana = 3

wynik = binary_search(moja_lista, szukana)

if wynik != -1:
    print(f"Liczba {szukana} znajduje się pod indeksem {wynik}")
else:
    print("Nie znaleziono liczby w liście")