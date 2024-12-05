import random
class Wartownik:
    def __init__(self):
        self.tablica = []

    def wypelnij(self):
        for i in range(50):
            liczba = random.randint(1,100)
            self.tablica.append(liczba)

    def wypiszTablice(self):
        for i in range(50):
            print(self.tablica[i], end=' ')

    def wyszukaj(self, wdz):
        value=0
        self.tablica.append(wdz)
        for i in range(len(self.tablica)):
                if self.tablica[i-1]==wdz:
                    value=i+1
                    break
        return value;

if __name__ == "__main__":
    wartownik = Wartownik()
    wartownik.wypelnij()
    wartownik.wypiszTablice()
    print()
    wartoscdoznalezienia = int(input("Podaj wartość do znalezienia w tablicy: "))
    pozycja = wartownik.wyszukaj(wartoscdoznalezienia)
    if pozycja == 0:
        print("Nie znaleziono wartości w tablicy.")
    else:
        print(f"Znaleziono wartość na pozycji: {pozycja}")