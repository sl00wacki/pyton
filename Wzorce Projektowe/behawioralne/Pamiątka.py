# Edytor (źródło) przechowuje dane, które mogą się zmieniać
class Editor:
    def __init__(self):
        self.text = ""
        self.curX = 0
        self.curY = 0
        self.selectionWidth = 0

    def setText(self, text):
        self.text = text

    def setCursor(self, x, y):
        self.curX = x
        self.curY = y

    def setSelectionWidth(self, width):
        self.selectionWidth = width

    # Tworzy snapshot (pamiątkę) bieżącego stanu
    def createSnapshot(self):
        return Snapshot(self, self.text, self.curX, self.curY, self.selectionWidth)


# Pamiątka przechowuje stan edytora, aby mogła go później przywrócić
class Snapshot:
    def __init__(self, editor, text, curX, curY, selectionWidth):
        self.editor = editor
        self.text = text
        self.curX = curX
        self.curY = curY
        self.selectionWidth = selectionWidth

    # Przywraca stan edytora do stanu zapisanej pamiątki
    def restore(self):
        self.editor.setText(self.text)
        self.editor.setCursor(self.curX, self.curY)
        self.editor.setSelectionWidth(self.selectionWidth)


# Polecenie zapisuje stan edytora przed zmianą i umożliwia wycofanie zmiany
class Command:
    def __init__(self, editor):
        self.editor = editor
        self.backup = None

    # Tworzy kopię zapasową stanu edytora
    def makeBackup(self):
        self.backup = self.editor.createSnapshot()

    # Przywraca stan edytora na podstawie kopii zapasowej
    def undo(self):
        if self.backup is not None:
            self.backup.restore()

    # Operacja wykonująca zmianę, może być różna dla różnych poleceń
    def execute(self):
        raise NotImplementedError("Must implement execute method in subclasses")


# Przykładowa operacja (zmiana tekstu) w edytorze
class ChangeTextCommand(Command):
    def __init__(self, editor, newText):
        super().__init__(editor)
        self.newText = newText

    def execute(self):
        self.makeBackup()
        print(f"Changing text to: {self.newText}")
        self.editor.setText(self.newText)


# Użycie przykładowe:

# Tworzenie edytora i poleceń
editor = Editor()
editor.setText("Initial text")
editor.setCursor(5, 10)
editor.setSelectionWidth(3)

# Tworzenie polecenia zmiany tekstu
command = ChangeTextCommand(editor, "Updated text")

# Wykonanie polecenia zmiany tekstu
command.execute()

# Sprawdzenie zmienionego stanu
print(f"Editor state after change: {editor.text}")

# Cofnięcie zmiany
command.undo()

# Sprawdzenie stanu po wycofaniu zmiany
print(f"Editor state after undo: {editor.text}")
