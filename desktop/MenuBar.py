import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenuBar

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Okno z Menu")
        self.setGeometry(100, 100, 400, 300)

        # Tworzenie menu
        menubar = self.menuBar()
        file_menu = menubar.addMenu('Plik')

        # Tworzenie akcji w menu
        new_action = QAction('Nowy', self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

    def new_file(self):
        print("Nowy plik")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
