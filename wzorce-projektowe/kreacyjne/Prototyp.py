from copy import deepcopy

# Bazowy prototyp
class Shape:
    def __init__(self, x=0, y=0, color=""):
        self.x = x
        self.y = y
        self.color = color

    def __init_from_shape__(self, source):
        self.x = source.x
        self.y = source.y
        self.color = source.color

    def clone(self):
        raise NotImplementedError("Clone method should be implemented in subclasses")


# Konkretne prototypy
class Rectangle(Shape):
    def __init__(self, x=0, y=0, color="", width=0, height=0):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def __init_from_shape__(self, source):
        super().__init_from_shape__(source)
        self.width = source.width
        self.height = source.height

    def clone(self):
        clone = Rectangle()
        clone.__init_from_shape__(self)
        return clone


class Circle(Shape):
    def __init__(self, x=0, y=0, color="", radius=0):
        super().__init__(x, y, color)
        self.radius = radius

    def __init_from_shape__(self, source):
        super().__init_from_shape__(source)
        self.radius = source.radius

    def clone(self):
        clone = Circle()
        clone.__init_from_shape__(self)
        return clone


# Klient
class Application:
    def __init__(self):
        self.shapes = []

        circle = Circle(x=10, y=10, radius=20, color="red")
        self.shapes.append(circle)

        another_circle = circle.clone()
        self.shapes.append(another_circle)

        rectangle = Rectangle(x=5, y=5, width=10, height=20, color="blue")
        self.shapes.append(rectangle)

    def business_logic(self):
        shapes_copy = []

        # Tworzenie kopii wszystkich obiektów w liście shapes
        for shape in self.shapes:
            shapes_copy.append(shape.clone())

        return shapes_copy

if __name__ == "__main__":
    app = Application()
    print("Oryginalne figury:")
    for shape in app.shapes:
        print(vars(shape))

    shapes_copy = app.business_logic()
    print("\nKlonowane figury:")
    for shape in shapes_copy:
        print(vars(shape))
