def scal(tablica, lewy, srodek, prawy):
    rozmiar1 = srodek-lewy+1
    rozmiar2 = prawy-srodek

    lewaCzesc = tablica[lewy:srodek+1]
    prawaCzesc = tablica[srodek+1:prawy+1]

    i=0
    j=0
    while i < rozmiar1 and j < rozmiar2:
        if lewaCzesc[i] <= prawaCzesc[j]:
            tablica[lewy] = lewaCzesc[i]
            i+=1
        else:
            tablica[lewy] = prawaCzesc[j]
            j+=1
        lewy+=1

    while i<rozmiar1:
        tablica[lewy] = lewaCzesc[i]
        i+=1
        lewy+=1
    while j<rozmiar2:
        tablica[lewy] = prawaCzesc[j]
        j+=1
        lewy+=1

def sortowanie_przez_scalanie(zbior,lewy, prawy):
    if lewy<prawy:
        srodek=(lewy+prawy)//2
        sortowanie_przez_scalanie(zbior,lewy,srodek)
        sortowanie_przez_scalanie(zbior, srodek+1, prawy)
        scal(zbior,lewy,srodek,prawy)

tablica = [9, 5, 21, 4, 5, 1, 515, 12, 5, 1, 6, 6, 1]
sortowanie_przez_scalanie(tablica, 0, len(tablica)-1)

# Print sorted array
for i in tablica:
    print(i, end=' ')