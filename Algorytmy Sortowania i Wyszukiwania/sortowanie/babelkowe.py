# Sortowanie bąbelkowe (Bubble Sort):
# Działanie: Przechodzi przez listę, porównując i zamieniając sąsiednie elementy, aż lista jest posortowana.
# Złożoność:
 #       Czasowa: O(n²).
  #      Pamięciowa: O(1).
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
