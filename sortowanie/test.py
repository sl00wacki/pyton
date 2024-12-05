from turtledemo.penrose import start


class SortowaniePrzezWybieranie:
    def __init__(self):
        self.tablica=[]
    def wczytaj_tablice(self):
        for i in range(10):
            liczba = int(input(f"Wprowadź liczbę {i + 1}: "))
            self.tablica.append(liczba)
    def sortuj(self):
        for i in range(len(self.tablica)-1):
            indeks_max = self.szukaj_najwyzszej(i)
            self.tablica[i], self.tablica[indeks_max] = self.tablica[indeks_max], self.tablica[i]
    def szukaj_najwyzszej(self, start):
        indeks_max = start
        for j in range(start +1, len(self.tablica)):
            if self.tablica[j] > self.tablica[indeks_max]:
                indeks_max = j
        return indeks_max
    def wyswietl(self):
        for i in self.tablica:
            print(i, end=' ')

if __name__ == "__main__":
    sortowanie = SortowaniePrzezWybieranie()
    sortowanie.wczytaj_tablice()
    sortowanie.sortuj()
    sortowanie.wyswietl()