class Euklides:
    def NWD(self,a,b):
        while(a!=b):
            if(a>b):
                a=a-b
            else:
                b=b-a
        return a
if __name__ == "__main__":
    euklides = Euklides()
    while True:
        try:
            pierwsza = int(input("Wprowadz pierwszą liczbę calkowita (musi byc dodatnia): "))
            druga = int(input("Wprowadz druga liczbe calkowita (musi byc dodatnia): "))
            if pierwsza > 0 and druga >0:
                break
            else:
                print("Obie liczby musza byc dodatnie")
        except ValueError:
            print("Obie wartosci musza byc calkowite")
    wynik = euklides.NWD(pierwsza,druga)
    print(wynik)

