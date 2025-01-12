# Sortowanie przez wstawianie (Insertion Sort):
# Działanie: Iteracyjnie wstawia każdy element w odpowiednie miejsce w posortowanej części listy.
# Złożoność:
        #Czasowa: O(n²) w najgorszym przypadku, O(n) w najlepszym.
        #Pamięciowa: O(1).

def sortowanie_przez_wstawianie():
    for i in range(len(tablica)):
        klucz = tablica[i]
        j=i-1
        while j>= 0 and tablica[j]>klucz:
            tablica[j+1] = tablica[j]
            j-=1
        tablica[j+1] = klucz

tablica = [9, 5, 21, 4, 5, 1, 515, 12, 5, 1, 6, 6, 1]
sortowanie_przez_wstawianie()
for i in tablica:
    print(i, end=' ')