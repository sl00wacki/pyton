import random
class Generator:
    def __init__(self):
        self.kod = ""
        self.CharacterLetters = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
        self.CharacterNumber = "1234567890"

    def generator(self, dlugosc, czyzliterami):
        self.kod = ""
        for i in range(dlugosc):
            if czyzliterami:
                self.kod += random.choice(self.CharacterLetters)
            else:
                self.kod += random.choice(self.CharacterNumber)
        print(f"Oto twój kod: {self.kod}")
        return(self.kod)


if __name__ == "__main__":
    g = Generator()
    dlugosc = int(input("Wprowadź długość kodu: "))
    czy = input("Czy kod ma być z literami?\nTrue - tak, False - nie\n")
    czyzLiterami = czy.lower() == "true"
    czy = input("Czy zapisac kod w pliku?\nTrue - tak, False - nie\n")
    if czy=="True":
        with open("pliki/kod.txt", 'w', encoding='utf-8') as plik:
            plik.write(g.generator(dlugosc, czyzLiterami))
