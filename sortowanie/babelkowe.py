
# Złożoność obliczeniowa równa O(i^2).
def sortowanie_babelkowe(tablica):
    for i in range(len(tablica)):
        for j in range(1, len(tablica) - i):
            if tablica[j-1] > tablica[j]:
                tablica[j-1], tablica[j] = tablica[j], tablica[j-1]
    return tablica

tablica = [9, 5, 21, 4, 5, 1, 515, 12, 5, 1, 6, 6, 1]
sortowanie_babelkowe(tablica)
for i in tablica:
    print(i, end=' ')
