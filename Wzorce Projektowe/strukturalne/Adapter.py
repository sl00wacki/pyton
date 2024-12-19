import math

# Klasa reprezentująca okrągły otwór.
class RoundHole:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def fits(self, peg):
        return self.get_radius() >= peg.get_radius()


# Klasa reprezentująca okrągły klocek.
class RoundPeg:
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius


# Klasa reprezentująca kwadratowy klocek.
class SquarePeg:
    def __init__(self, width):
        self._width = width

    def get_width(self):
        return self._width


# Klasa adaptera pozwalająca na dopasowanie kwadratowego klocka do okrągłego otworu.
class SquarePegAdapter(RoundPeg):
    def __init__(self, square_peg):
        # Przekazujemy kwadratowy klocek do adaptera.
        self._square_peg = square_peg

    def get_radius(self):
        # Obliczamy promień okręgu opisującego kwadrat.
        return self._square_peg.get_width() * math.sqrt(2) / 2


# Kod klienta
if __name__ == "__main__":
    # Tworzymy okrągły otwór o promieniu 5.
    hole = RoundHole(5)

    # Tworzymy okrągły klocek o promieniu 5.
    rpeg = RoundPeg(5)
    print(hole.fits(rpeg))  # True

    # Tworzymy kwadratowe klocki o boku 5 i 10.
    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)

    # Próba dopasowania kwadratowych klocków bez adaptera.
    # print(hole.fits(small_sqpeg))  # Błąd, bo SquarePeg nie ma metody `get_radius`.

    # Użycie adaptera do dopasowania kwadratowych klocków.
    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)

    print(hole.fits(small_sqpeg_adapter))  # True
    print(hole.fits(large_sqpeg_adapter))  # False
