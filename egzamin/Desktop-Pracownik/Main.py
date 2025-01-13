import sys, random
from PyQt5 import QtWidgets, uic

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('untitled.ui', self)

        # Dane pracownika
        self.lineEdit_Imie = self.findChild(QtWidgets.QLineEdit, "lineEdit_Imie")
        self.lineEdit_Nazwisko = self.findChild(QtWidgets.QLineEdit, "lineEdit_Nazwisko")
        self.comboBox_Stanowisko = self.findChild(QtWidgets.QComboBox, "comboBox_Stanowisko")

        # Zmienne do hasła
        self.checkBox_Maleiwielkie = self.findChild(QtWidgets.QCheckBox, "checkBox_Maleiwielkie")
        self.checkBox_Cyfry = self.findChild(QtWidgets.QCheckBox, "checkBox_Cyfry")
        self.checkBox_Znaki_specjalne = self.findChild(QtWidgets.QCheckBox, "checkBox_Znaki_specjalne")
        self.lineEdit_IleZnakow = self.findChild(QtWidgets.QLineEdit, "lineEdit_IleZnakow")

        # Przyciski
        self.button_generuj_haslo = self.findChild(QtWidgets.QPushButton, "pushButton_generuj_haslo")
        self.button_generuj_haslo.clicked.connect(self.generuj_haslo)

        self.pushButton_zatwierdz = self.findChild(QtWidgets.QPushButton, "pushButton_zatwierdz")
        self.pushButton_zatwierdz.clicked.connect(self.zatwierdz)

        self.show()

    # **********************************************
    # nazwa funkcji: generuj_haslo
    # opis funkcji: Funkcja generuje hasło, które wyświetla w oknie dialogowym. W zależności od naciśniętych CheckBoxów, dodaje do niego po jednej z typu znaków, którą zaznaczył użytkownik
    # parametry: brak
    # zwracany typ i opis: brak – funkcja wykonuje akcje bez zwracania wartości.
    # autor: <numer zdającego>
    # **********************************************

    def generuj_haslo(self):
        ileZnakow = 0
        password= []
        charSet = "abcdefghijklmnopqrstuvwxyz"
        ileZnakow = int(self.lineEdit_IleZnakow.text())

        if self.checkBox_Maleiwielkie.isChecked():
            password.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
            ileZnakow -= 1

        if self.checkBox_Cyfry.isChecked():
            password.append(random.choice("0123456789"))
            ileZnakow -= 1

        if self.checkBox_Znaki_specjalne.isChecked():
            password.append(random.choice("!@#$%^&*()_+-="))
            ileZnakow -= 1

        for i in range(ileZnakow):
            password.append(random.choice(charSet))

        random.shuffle(password)

        self.password = ""
        for char in password:
            self.password += char

        msgbox = QtWidgets.QMessageBox()
        msgbox.setText(f"Wygenerowane hasło: {self.password}")
        msgbox.setWindowTitle("Hasło")
        msgbox.exec_()

    # **********************************************
    # nazwa funkcji: zatwierdz
    # opis funkcji: Funkcja wyświetla podane przez użytkownika dane pracownika jak i wygenerowane (bądź nie) hasło w oknie dialogowym.
    # parametry: brak
    # zwracany typ i opis: brak – funkcja wykonuje akcje bez zwracania wartości.
    # autor: <numer zdającego>
    # **********************************************

    def zatwierdz(self):
        imie = self.lineEdit_Imie.text()
        nazwisko = self.lineEdit_Nazwisko.text()
        stanowisko = self.comboBox_Stanowisko.currentText()

        msgbox = QtWidgets.QMessageBox()
        msgbox.setText(
            f"Dane pracownika: {imie} {nazwisko} {stanowisko} Hasło: {self.password}"
        )
        msgbox.setWindowTitle("Dane Pracownika")
        msgbox.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    sys.exit(app.exec_())
