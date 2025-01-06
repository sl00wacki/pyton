import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moje Okno Aplikacji")
        self.setGeometry(100, 100, 400, 300)  # Określamy pozycję i rozmiar okna

        # Dodajemy przycisk do okna
        button = QPushButton('Kliknij mnie', self)
        button.clicked.connect(self.on_click)
        button.setGeometry(150, 100, 100, 50)

    def on_click(self):
        print("Przycisk kliknięty!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
