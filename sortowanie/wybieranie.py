def sortowanie_przez_wybieranie():
    for i in range(len(tablica)-1):
        indeks_min = i
        for j in range(i+1, len(tablica)):
            if tablica[j] < tablica[indeks_min]:
                indeks_min=j
            tablica[i], tablica[indeks_min] = tablica[indeks_min], tablica[i]


tablica = [9, 5, 21, 4, 5, 1, 515, 12, 5, 1, 6, 6, 1]
sortowanie_przez_wybieranie()
for i in tablica:
    print(i, end=' ')