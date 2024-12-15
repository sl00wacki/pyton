class Film:
    def __init__(self):
        self.title=""
        self.numberOfRentals=0
    def setTitle(self, title):
        self.title=title
    def getTitle(self):
        return self.title
    def getNumberofRentals(self):
        return self.numberOfRentals
    def incrementNumberOfRentals(self):
        self.numberOfRentals+=1

if __name__ == "__main__":
    film = Film()
    print(f"Nazwa filmu przed: {film.getTitle()}\nLiczba wypozyczen: {film.getNumberofRentals()}")
    film.setTitle("Gladiator II")
    for i in range(10):
        film.incrementNumberOfRentals()
    print(f"Nazwa filmu po: {film.getTitle()}\nLiczba wypożyczeń: {film.getNumberofRentals()}")

