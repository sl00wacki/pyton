from abc import ABC, abstractmethod

# Klasa abstrakcyjna dla produktów (przycisków)
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self, callback):
        pass

# Konkretny produkt: przycisk dla Windows
class WindowsButton(Button):
    def render(self):
        print("Renderuję przycisk w stylu Windows")

    def on_click(self, callback):
        print("Przycisk Windows został kliknięty")
        callback()

# Konkretny produkt: przycisk HTML
class HTMLButton(Button):
    def render(self):
        print("Renderuję przycisk HTML")

    def on_click(self, callback):
        print("Przycisk HTML został kliknięty")
        callback()

# Twórca (Creator)
class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    def render(self):
        button = self.create_button()
        button.render()
        button.on_click(self.close_dialog)

    def close_dialog(self):
        print("Dialog został zamknięty.")

# Konkretny twórca: WindowsDialog
class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()

# Konkretny twórca: WebDialog
class WebDialog(Dialog):
    def create_button(self) -> Button:
        return HTMLButton()

# Aplikacja
def application(os_type):
    if os_type == "Windows":
        dialog = WindowsDialog()
    elif os_type == "Web":
        dialog = WebDialog()
    else:
        raise ValueError("Nieznany typ systemu operacyjnego")

    dialog.render()

if __name__ == "__main__":
    application("Windows")
    print("---")
    application("Web")
