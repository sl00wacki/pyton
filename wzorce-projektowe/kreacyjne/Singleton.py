import threading

class Database:
    # Statyczne pole przechowujące instancję singletona.
    _instance = None
    _lock = threading.Lock()  # Blokada dla zapewnienia bezpieczeństwa wątków.

    # Prywatny konstruktor
    def __init__(self):
        if Database._instance is not None:
            raise Exception("Ten obiekt jest singletonem! Użyj get_instance().")
        # Kod inicjalizacyjny, np. połączenie z bazą danych.
        print("Inicjalizacja połączenia z bazą danych.")

    # Statyczna metoda dostępu do instancji singletona.
    @staticmethod
    def get_instance():
        if Database._instance is None:
            with Database._lock:
                if Database._instance is None:  # Ponowna weryfikacja po uzyskaniu blokady.
                    Database._instance = Database()
        return Database._instance

    # Przykładowa metoda biznesowa singletona.
    def query(self, sql):
        print(f"Wykonywanie zapytania: {sql}")


# Klasa aplikacji (klient)
class Application:
    def main(self):
        # Uzyskanie instancji singletona
        db1 = Database.get_instance()
        db1.query("SELECT * FROM users")

        # Uzyskanie tej samej instancji w innym miejscu
        db2 = Database.get_instance()
        db2.query("SELECT * FROM orders")

        # Dowód, że obie zmienne odnoszą się do tej samej instancji
        print(f"Czy db1 i db2 to ta sama instancja? {db1 is db2}")


if __name__ == "__main__":
    app = Application()
    app.main()
