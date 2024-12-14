from abc import ABC, abstractmethod
from typing import List

# Interfejs Shape - element
class Shape(ABC):
    @abstractmethod
    def move(self, x: int, y: int):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def accept(self, v: 'Visitor'):
        pass

# Konkretne klasy elementów

class Dot(Shape):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Drawing a dot at ({self.x}, {self.y})")

    def accept(self, v: 'Visitor'):
        v.visitDot(self)

class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int):
        self.x = x
        self.y = y
        self.radius = radius

    def move(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Drawing a circle at ({self.x}, {self.y}) with radius {self.radius}")

    def accept(self, v: 'Visitor'):
        v.visitCircle(self)

class Rectangle(Shape):
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, x: int, y: int):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Drawing a rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}")

    def accept(self, v: 'Visitor'):
        v.visitRectangle(self)

class CompoundShape(Shape):
    def __init__(self):
        self.shapes: List[Shape] = []

    def add(self, shape: Shape):
        self.shapes.append(shape)

    def move(self, x: int, y: int):
        for shape in self.shapes:
            shape.move(x, y)

    def draw(self):
        for shape in self.shapes:
            shape.draw()

    def accept(self, v: 'Visitor'):
        v.visitCompoundShape(self)

# Interfejs odwiedzającego
class Visitor(ABC):
    @abstractmethod
    def visitDot(self, d: Dot):
        pass

    @abstractmethod
    def visitCircle(self, c: Circle):
        pass

    @abstractmethod
    def visitRectangle(self, r: Rectangle):
        pass

    @abstractmethod
    def visitCompoundShape(self, cs: CompoundShape):
        pass

# Konkretna implementacja odwiedzającego - eksport do XML
class XMLExportVisitor(Visitor):
    def visitDot(self, d: Dot):
        print(f"Exporting Dot with coordinates ({d.x}, {d.y})")

    def visitCircle(self, c: Circle):
        print(f"Exporting Circle with center ({c.x}, {c.y}) and radius {c.radius}")

    def visitRectangle(self, r: Rectangle):
        print(f"Exporting Rectangle with top-left ({r.x}, {r.y}), width {r.width}, and height {r.height}")

    def visitCompoundShape(self, cs: CompoundShape):
        print("Exporting CompoundShape with the following shapes:")
        for shape in cs.shapes:
            shape.accept(self)  # Rekursywnie odwiedzamy elementy złożonej figury

# Aplikacja, która wykorzystuje wzorzec odwiedzającego
class Application:
    def __init__(self):
        self.all_shapes: List[Shape] = []

    def export(self):
        export_visitor = XMLExportVisitor()
        for shape in self.all_shapes:
            shape.accept(export_visitor)

# Przykładowe użycie
if __name__ == "__main__":
    # Tworzymy różne kształty
    dot = Dot(1, 2)
    circle = Circle(3, 4, 5)
    rectangle = Rectangle(6, 7, 8, 9)
    compound_shape = CompoundShape()
    compound_shape.add(dot)
    compound_shape.add(circle)

    # Tworzymy aplikację
    app = Application()

    # Dodajemy kształty do aplikacji
    app.all_shapes.append(dot)
    app.all_shapes.append(circle)
    app.all_shapes.append(rectangle)
    app.all_shapes.append(compound_shape)

    # Eksportujemy kształty
    app.export()
