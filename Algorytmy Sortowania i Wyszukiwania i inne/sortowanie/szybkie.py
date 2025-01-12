# Sortowanie szybkie (Quick Sort):
# Działanie: Dzieli listę wokół pivotu, rekurencyjnie sortując podlisty.
# Złożoność:
  #      Czasowa: O(n log n) średnio, O(n²) w najgorszym przypadku.
   #     Pamięciowa: O(log n) (rekurencja).

def sortowanie_szybkie(tablica, lewy, prawy):
    i = lewy
    j = prawy
    os = tablica[(lewy + prawy) // 2]

    while i <= j:
        while i <= prawy and tablica[i] < os:
            i += 1
        while j >= lewy and tablica[j] > os:
            j -= 1
        if i <= j:
            tablica[i], tablica[j] = tablica[j], tablica[i]
            i += 1
            j -= 1

    if lewy < j:
        sortowanie_szybkie(tablica, lewy, j)
    if i < prawy:
        sortowanie_szybkie(tablica, i, prawy)

# Example usage
tablica = [9, 5, 21, 4, 5, 1, 515, 12, 5, 1, 6, 6, 1]
sortowanie_szybkie(tablica, 0, len(tablica) - 1)

# Print sorted array
for i in tablica:
    print(i, end=' ')
