from typing import List

# Klasa pyłek przechowująca wspólny stan
class TreeType:
    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x: int, y: int):
        # Narysuj drzewo na ekranie w punkcie (x, y)
        print(f"Drawing {self.name} tree with color {self.color} and texture {self.texture} at ({x}, {y})")

# Fabryka pyłków odpowiedzialna za zarządzanie instancjami TreeType
class TreeFactory:
    # Kolekcja przechowująca unikalne typy drzew (wspólny stan)
    tree_types: List[TreeType] = []

    @staticmethod
    def get_tree_type(name: str, color: str, texture: str) -> TreeType:
        # Szukaj, czy taki typ drzewa już istnieje
        for tree_type in TreeFactory.tree_types:
            if (tree_type.name == name and
                tree_type.color == color and
                tree_type.texture == texture):
                return tree_type
        # Jeśli nie ma, twórz nowy i dodaj do kolekcji
        new_tree_type = TreeType(name, color, texture)
        TreeFactory.tree_types.append(new_tree_type)
        return new_tree_type

# Klasa Tree zawierająca specyficzny stan drzewa (współrzędne)
class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self, canvas):
        # Rysowanie drzewa z użyciem typu (TreeType)
        self.tree_type.draw(canvas, self.x, self.y)

# Klasa Forest, która przechowuje wszystkie drzewa w lesie
class Forest:
    def __init__(self):
        self.trees: List[Tree] = []

    def plant_tree(self, x: int, y: int, name: str, color: str, texture: str):
        # Uzyskiwanie odpowiedniego typu drzewa z fabryki
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        # Tworzenie nowego drzewa z konkretnymi współrzędnymi
        tree = Tree(x, y, tree_type)
        # Dodanie drzewa do lasu
        self.trees.append(tree)

    def draw(self, canvas):
        # Rysowanie wszystkich drzew w lesie
        for tree in self.trees:
            tree.draw(canvas)

# Przykład użycia
if __name__ == "__main__":
    # Tworzymy las
    forest = Forest()

    # Dodajemy drzewa do lasu (współdzielą ten sam typ drzewa)
    forest.plant_tree(1, 2, "Oak", "Green", "Rough")
    forest.plant_tree(3, 4, "Oak", "Green", "Rough")
    forest.plant_tree(5, 6, "Pine", "Dark Green", "Smooth")

    # Rysowanie lasu
    forest.draw("Canvas1")
