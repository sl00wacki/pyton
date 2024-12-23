class Pesel:
    def __init__(self, pesel):
        self.pesel = pesel
    def sprawdzPlec(self):
        if self.pesel.endswith("0") or self.pesel.endswith("2") or self.pesel.endswith("4") or self.pesel.endswith("6") or self.pesel.endswith("8"):
           plec = "K"
        else:
            plec = "M"
        return plec

    def sprawdzSumeKontrolna(self):
        s=0
        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        for i in range(10):
             s +=(int(self.pesel[i]) * weights[i])
        m = s%10
        r = 10-m
        if self.pesel.endswith(str(r)):
            return True
        else:
            return False

if __name__ == "__main__":
    pesel = input("Wprowadź pesel (11 cyfr):\n")
    p3sel = Pesel(pesel)
    print("Plec: ")
    plec = p3sel.sprawdzPlec()
    if plec=="M":
        print("Mężczyzna")
    else:
        print("Kobieta")
    print("Czy pesel jest poprawny: ")
    print(p3sel.sprawdzSumeKontrolna())