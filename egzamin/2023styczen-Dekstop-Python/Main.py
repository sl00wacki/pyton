import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('untitled.ui', self)

        # Check price button
        self.button_check_price = self.findChild(QtWidgets.QPushButton, 'pushButton_check_price')
        self.button_check_price.clicked.connect(self.check_price)

        # Apply button (fixing the connection)
        self.button_apply = self.findChild(QtWidgets.QPushButton, 'pushButton_apply')
        self.button_apply.clicked.connect(self.check_address)  # Corrected to call check_address

        # Group box for parcel type
        self.groupbox_type_of_parcel = self.findChild(QtWidgets.QGroupBox, 'groupBox_parcel_type')

        # Inputs
        self.input_street = self.findChild(QtWidgets.QLineEdit, 'lineEdit_street')
        self.input_postal_code = self.findChild(QtWidgets.QLineEdit, 'lineEdit_postal_code')
        self.input_city = self.findChild(QtWidgets.QLineEdit, 'lineEdit_city')

        # Labels
        self.label_img = self.findChild(QtWidgets.QLabel, 'label_img')
        self.label_price = self.findChild(QtWidgets.QLabel, 'label_price')

        self.show()

    def check_price(self):
        parcels = {
            "Pocztówka": ["1 zł", "pocztowka.png"],
            "List": ["1,5 zł", "list.png"],
            "Paczka": ["10 zł", "paczka.png"]
        }

        # Find the selected radio button text
        selected_parcel_type = None
        for button in self.groupbox_type_of_parcel.findChildren(QtWidgets.QRadioButton):
            if button.isChecked():
                selected_parcel_type = button.text()
                break

        if selected_parcel_type in parcels:
            price, image = parcels[selected_parcel_type]
            self.label_price.setText(f"Cena: {price}")
            self.label_img.setPixmap(QPixmap(image))

    def check_address(self):
        postal_code = self.input_postal_code.text()
        msg = "Dane przesyłki zostały wprowadzone"
        if len(postal_code) != 5:
            msg = "Nieprawidłowy kod pocztowy - nieprawidłowa liczba cyfr!"
        elif not postal_code.isnumeric():
            msg = "Kod pocztowy powinien składać się z samych cyfr!"

        msgbox = QtWidgets.QMessageBox()
        msgbox.setText(msg)
        msgbox.setWindowTitle("Informacja")
        msgbox.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
