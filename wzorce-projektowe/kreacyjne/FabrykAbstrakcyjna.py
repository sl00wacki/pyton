from abc import ABC, abstractmethod

# Interfejs fabryki abstrakcyjnej
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Konkretna fabryka dla Windows
class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()

# Konkretna fabryka dla macOS
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()

# Interfejs przycisku
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

# Konkretne implementacje przycisku
class WinButton(Button):
    def paint(self):
        print("Renderuję przycisk w stylu Windows.")

class MacButton(Button):
    def paint(self):
        print("Renderuję przycisk w stylu macOS.")

# Interfejs pola wyboru (Checkbox)
class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

# Konkretne implementacje pola wyboru
class WinCheckbox(Checkbox):
    def paint(self):
        print("Renderuję pole wyboru w stylu Windows.")

class MacCheckbox(Checkbox):
    def paint(self):
        print("Renderuję pole wyboru w stylu macOS.")

# Klasa aplikacji klienckiej
class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()

# Konfigurator aplikacji
def application_configurator(os_type):
    if os_type == "Windows":
        factory = WinFactory()
    elif os_type == "Mac":
        factory = MacFactory()
    else:
        raise Exception("Error! Unknown operating system.")

    app = Application(factory)
    app.create_ui()
    app.paint()

# Testowanie
if __name__ == "__main__":
    print("Konfiguracja dla Windows:")
    application_configurator("Windows")

    print("\nKonfiguracja dla macOS:")
    application_configurator("Mac")
