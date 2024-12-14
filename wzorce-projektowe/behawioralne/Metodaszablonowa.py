from abc import ABC, abstractmethod

# Klasa abstrakcyjna definiująca metodę szablonową
class GameAI(ABC):
    # Metoda szablonowa, która definiuje szkielet algorytmu
    def turn(self):
        self.collect_resources()
        self.build_structures()
        self.build_units()
        self.attack()

    # Domyślna implementacja metody collect_resources
    def collect_resources(self):
        for structure in self.built_structures:
            structure.collect()

    # Metody abstrakcyjne, które muszą zostać zaimplementowane przez konkretne klasy
    @abstractmethod
    def build_structures(self):
        pass

    @abstractmethod
    def build_units(self):
        pass

    @abstractmethod
    def send_scouts(self, position):
        pass

    @abstractmethod
    def send_warriors(self, position):
        pass

    # Domyślna implementacja ataku
    def attack(self):
        enemy = self.closest_enemy()
        if enemy is None:
            self.send_scouts(self.map.center)
        else:
            self.send_warriors(enemy.position)

    # Zwracanie mapy dla klas, które jej używają
    @property
    def map(self):
        # Mapa jest domyślnie obecna tylko w tych klasach, które jej potrzebują
        return type("Map", (), {"center": (0, 0)})


# Konkretna klasa implementująca AI dla orków
class OrcsAI(GameAI):
    def __init__(self):
        self.built_structures = []
        self.scouts = []
        self.warriors = []
        self.resources = 100  # Przykładowa ilość zasobów

    def build_structures(self):
        if self.resources > 50:
            print("Building farms, barracks, and fortress")
            self.built_structures.append("Farm")
            self.built_structures.append("Barracks")
            self.built_structures.append("Fortress")

    def build_units(self):
        if self.resources > 30:
            if len(self.scouts) == 0:
                print("Building foot soldier and adding to scouts group")
                self.scouts.append("Foot Soldier")
            else:
                print("Building warrior and adding to warriors group")
                self.warriors.append("Warrior")

    def send_scouts(self, position):
        if len(self.scouts) > 0:
            print(f"Sending scouts to {position}")

    def send_warriors(self, position):
        if len(self.warriors) > 5:
            print(f"Sending warriors to {position}")

    def closest_enemy(self):
        # Przykład, w rzeczywistej grze tu byłby kod do znalezienia wroga
        return None  # Zwracamy None dla uproszczenia


# Konkretna klasa implementująca AI dla potworów
class MonstersAI(GameAI):
    def __init__(self):
        self.built_structures = []
        self.scouts = []
        self.warriors = []

    def collect_resources(self):
        print("Monsters do not collect resources.")

    def build_structures(self):
        print("Monsters do not build structures.")

    def build_units(self):
        print("Monsters do not build units.")

    def send_scouts(self, position):
        print("Monsters do not send scouts.")

    def send_warriors(self, position):
        print("Monsters do not send warriors.")

    def closest_enemy(self):
        # W tej klasie możemy mieć inne zachowanie, np. losowe wybieranie wroga
        return None

    # Zdefiniowanie mapy, aby uniknąć błędu, gdy jest wywoływana w metodzie ataku
    @property
    def map(self):
        # Potwory nie mają mapy, ale musimy zapewnić, że map.center będzie dostępne
        return type("Map", (), {"center": (0, 0)})


# Przykład użycia:
if __name__ == "__main__":
    # AI dla orków
    orc_ai = OrcsAI()
    orc_ai.turn()

    print("\n")

    # AI dla potworów
    monster_ai = MonstersAI()
    monster_ai.turn()
