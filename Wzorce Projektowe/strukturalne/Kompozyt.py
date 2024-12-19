from typing import List

# Interfejs komponentu
class Graphic:
    def move(self, x: int, y: int):
        raise NotImplementedError()

    def draw(self):
        raise NotImplementedError()


# Klasa liść: Kropka
class Dot(Graphic):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, x: int, y: int):
        self.x += x
        self.y += y

    def draw(self):
        print(f"Rysowanie kropki w punkcie ({self.x}, {self.y})")


# Klasa liść: Okrąg
class Circle(Dot):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        print(f"Rysowanie okręgu w punkcie ({self.x}, {self.y}) o promieniu {self.radius}")


# Klasa kompozyt: Grupa graficzna
class CompoundGraphic(Graphic):
    def __init__(self):
        self.children: List[Graphic] = []

    def add(self, child: Graphic):
        self.children.append(child)

    def remove(self, child: Graphic):
        self.children.remove(child)

    def move(self, x: int, y: int):
        for child in self.children:
            child.move(x, y)

    def draw(self):
        print("Rysowanie grupy graficznej:")
        for child in self.children:
            child.draw()
        print("Zakończono rysowanie grupy")


# Klient: Edytor obrazów
class ImageEditor:
    def __init__(self):
        self.all = CompoundGraphic()

    def load(self):
        self.all = CompoundGraphic()
        self.all.add(Dot(1, 2))
        self.all.add(Circle(5, 3, 10))

    def group_selected(self, components: List[Graphic]):
        group = CompoundGraphic()
        for component in components:
            group.add(component)
            self.all.remove(component)
        self.all.add(group)
        self.all.draw()


# Kod klienta
if __name__ == "__main__":
    editor = ImageEditor()
    editor.load()
    editor.all.draw()  # Rysowanie wszystkich elementów.

    print("\nGrupowanie wybranych elementów...")
    selected_components = editor.all.children[:]
    editor.group_selected(selected_components)
