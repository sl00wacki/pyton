import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Okno z Dialogiem")
        self.setGeometry(100, 100, 400, 300)

        # Tworzymy przycisk, który wywoła dialog
        button = QPushButton('Pokaż dialog', self)
        button.clicked.connect(self.show_dialog)
        button.setGeometry(150, 100, 100, 50)

    def show_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("To jest komunikat!")
        msg.setWindowTitle("Komunikat")
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
