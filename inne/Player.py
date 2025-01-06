class Player:
    def __init__(self):
        self.name=""
        self.punkty=0
    def setPlayerName(self):
        self.name = input("Podaj nazwę gracza: ")

    def getPunkty(self):
        print(f"Ilośc punktów: {self.punkty}")

    def dodajPunkty(self, ilosc):
        print("Dodawanie punktów z bonusu!")
        self.punkty+=ilosc

    def odejmijPunkty(self, ilosc):
        print("Usuwanie puntków z pułapki!")
        self.punkty-=ilosc

    def pauseGame(self):
        print("Game paused...")

    def resumeGame(self):
        print("Game resumed...")

    def gameOver(self):
        print("Game over...")
if __name__ == "__main__":
    player = Player()
    player.setPlayerName()
    print("Zaczynanie gry...")
    player.dodajPunkty(10)
    player.getPunkty()
    player.odejmijPunkty(5)
    player.pauseGame()
    player.resumeGame()
    player.getPunkty()
    player.dodajPunkty(10)
    player.gameOver()
    player.getPunkty()


