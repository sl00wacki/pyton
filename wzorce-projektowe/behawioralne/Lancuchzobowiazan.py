# Interfejs obiektu obsługującego żądanie pomocy
from abc import ABC, abstractmethod


class ComponentWithContextualHelp(ABC):
    @abstractmethod
    def show_help(self):
        pass


# Klasa bazowa dla komponentów
class Component(ComponentWithContextualHelp):
    def __init__(self):
        self.tooltip_text = None
        self.container = None  # Odniesienie do kontenera

    # Metoda wyświetlająca pomoc
    def show_help(self):
        if self.tooltip_text:
            print(f"Showing tooltip: {self.tooltip_text}")
        elif self.container:
            self.container.show_help()


# Kontener dla komponentów
class Container(Component):
    def __init__(self):
        super().__init__()
        self.children = []  # Lista dzieci (komponentów)

    # Dodawanie komponentu do kontenera
    def add(self, child):
        self.children.append(child)
        child.container = self  # Ustawienie kontenera komponentu


# Komponent Button (przycisk)
class Button(Component):
    def __init__(self, x, y, width, height, text):
        super().__init__()
        self.tooltip_text = text


# Komponent Panel (panel)
class Panel(Container):
    def __init__(self):
        super().__init__()
        self.modal_help_text = None

    # Nadpisanie metody show_help, aby wyświetlić modalną pomoc
    def show_help(self):
        if self.modal_help_text:
            print(f"Displaying modal help: {self.modal_help_text}")
        else:
            super().show_help()


# Komponent Dialog (okno dialogowe)
class Dialog(Container):
    def __init__(self):
        super().__init__()
        self.wiki_page_url = None

    # Nadpisanie metody show_help, aby otworzyć stronę wiki z pomocą
    def show_help(self):
        if self.wiki_page_url:
            print(f"Opening help page: {self.wiki_page_url}")
        else:
            super().show_help()


# Klasa zarządzająca aplikacją
class Application:
    def create_ui(self):
        # Tworzenie komponentów interfejsu
        dialog = Dialog()
        dialog.wiki_page_url = "http://help.wiki/page"

        panel = Panel()
        panel.modal_help_text = "This panel does... something."

        ok = Button(250, 760, 50, 20, "OK")
        ok.tooltip_text = "This is an OK button that..."

        cancel = Button(320, 760, 50, 20, "Cancel")
        cancel.tooltip_text = "This is a Cancel button."

        # Dodanie przycisków do panelu
        panel.add(ok)
        panel.add(cancel)

        # Dodanie panelu do dialogu
        dialog.add(panel)

    # Metoda wywołująca pomoc przy naciśnięciu klawisza F1
    def on_f1_key_press(self):
        component = self.get_component_at_mouse_coords()
        component.show_help()

    # Symulacja funkcji wyszukiwania komponentu pod kursorem myszy
    def get_component_at_mouse_coords(self):
        # Tutaj po prostu zwróć pierwszy komponent (możesz to zmodyfikować)
        return self.get_first_component()

        # Metoda pomocnicza do uzyskania pierwszego komponentu

    def get_first_component(self):
        return Button(0, 0, 100, 30, "Test Button")


# Przykład uruchomienia aplikacji
app = Application()
app.create_ui()

# Symulacja naciśnięcia klawisza F1
app.on_f1_key_press()
