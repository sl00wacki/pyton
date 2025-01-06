import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Obsługa Zdarzeń")
        self.setGeometry(100, 100, 400, 300)

    def mousePressEvent(self, event):
        print("Kliknięto myszą!")

    def keyPressEvent(self, event):
        if event.key() == 16777220:  # Kod klawisza Enter
            print("Naciśnięto Enter!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
