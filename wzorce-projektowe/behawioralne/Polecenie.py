from abc import ABC, abstractmethod

# Bazowa klasa Command definiująca wspólny interfejs dla wszystkich poleceń
class Command(ABC):
    def __init__(self, app, editor):
        self.app = app
        self.editor = editor
        self.backup = None

    # Zrób kopię zapasową stanu edytora
    def save_backup(self):
        self.backup = self.editor.text

    # Przywróć stan edytora
    def undo(self):
        self.editor.text = self.backup

    # Metoda wykonująca zadanie, która musi być zaimplementowana przez konkretne polecenia
    @abstractmethod
    def execute(self):
        pass


# Konkretny typ polecenia: Copy
class CopyCommand(Command):
    def execute(self):
        self.app.clipboard = self.editor.get_selection()
        return False  # Nie zmienia stanu edytora


# Konkretny typ polecenia: Cut
class CutCommand(Command):
    def execute(self):
        self.save_backup()
        self.app.clipboard = self.editor.get_selection()
        self.editor.delete_selection()
        return True  # Zmienia stan edytora


# Konkretny typ polecenia: Paste
class PasteCommand(Command):
    def execute(self):
        self.save_backup()
        self.editor.replace_selection(self.app.clipboard)
        return True  # Zmienia stan edytora


# Konkretny typ polecenia: Undo
class UndoCommand(Command):
    def execute(self):
        self.app.undo()
        return False  # Nie zmienia stanu edytora


# Historia poleceń (stós)
class CommandHistory:
    def __init__(self):
        self.history = []

    def push(self, command):
        self.history.append(command)

    def pop(self):
        if self.history:
            return self.history.pop()
        return None


# Klasa edytora, która realizuje operacje na tekście
class Editor:
    def __init__(self):
        self.text = ""

    def get_selection(self):
        # Zwraca zaznaczony tekst, tu dla uproszczenia zakładając stały tekst
        return "Selected Text"

    def delete_selection(self):
        # Kasuje zaznaczony tekst
        self.text = self.text.replace(self.get_selection(), "")

    def replace_selection(self, new_text):
        # Zastępuje zaznaczony tekst nowym
        self.text = new_text


# Aplikacja, która łączy polecenia z interfejsem użytkownika
class Application:
    def __init__(self):
        self.clipboard = ""
        self.editors = [Editor()]
        self.active_editor = self.editors[0]
        self.history = CommandHistory()

    def create_ui(self):
        # Przypisanie poleceń do przycisków i skrótów
        copy = lambda: self.execute_command(CopyCommand(self, self.active_editor))
        cut = lambda: self.execute_command(CutCommand(self, self.active_editor))
        paste = lambda: self.execute_command(PasteCommand(self, self.active_editor))
        undo = lambda: self.execute_command(UndoCommand(self, self.active_editor))

        # Symulacja przypisania do przycisków
        print("UI Created: Buttons and Shortcuts Assigned")

    def execute_command(self, command):
        if command.execute():
            self.history.push(command)

    def undo(self):
        command = self.history.pop()
        if command:
            command.undo()


# Testowanie
app = Application()
app.create_ui()

# Symulacja działania przycisków
print("Initial Text:", app.active_editor.text)
app.active_editor.text = "Hello, World!"  # Ustawiamy początkowy tekst
print("Text after modification:", app.active_editor.text)

# Symulacja działań
cut = CutCommand(app, app.active_editor)
cut.execute()
print("Text after Cut:", app.active_editor.text)

app.undo()  # Cofanie operacji
print("Text after Undo:", app.active_editor.text)

paste = PasteCommand(app, app.active_editor)
paste.execute()
print("Text after Paste:", app.active_editor.text)

app.undo()  # Cofanie operacji
print("Text after Undo Paste:", app.active_editor.text)
