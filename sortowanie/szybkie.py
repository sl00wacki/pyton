def sortowanie_szybkie(tablica, lewy, prawy):
    i = lewy
    j = prawy
    os = tablica[(lewy + prawy) // 2]  # Pivot element

    while i <= j:
        while i <= prawy and tablica[i] < os:  # Bounds check for i
            i += 1
        while j >= lewy and tablica[j] > os:  # Bounds check for j
            j -= 1
        if i <= j:
            tablica[i], tablica[j] = tablica[j], tablica[i]
            i += 1
            j -= 1

    if lewy < j:
        sortowanie_szybkie(tablica, lewy, j)  # Sort left sub-array
    if i < prawy:
        sortowanie_szybkie(tablica, i, prawy)  # Sort right sub-array

# Example usage
tablica = [9, 5, 21, 4, 5, 1, 515, 12, 5, 1, 6, 6, 1]
sortowanie_szybkie(tablica, 0, len(tablica) - 1)

# Print sorted array
for i in tablica:
    print(i, end=' ')
