import sys


from PyQt5 import QtWidgets
from PyQt5 import uic

class MusicAlbum:
    # **********************************************
    # nazwa funkcji: __init__
    # opis funkcji: Konstruktor obiektu klasy MusicAlbum
    # parametry: artist_name - parametr przechowujący nazwę autora albumu
    #            album_name - parametr przechowujący nazwę albumu
    #            songs_numer - parametr przechowujący liczbę piosenek w albumie
    #            release_year - parametr przechowujący datę powstawnia albumu
    #            download_number - parametr przechowujący liczbę pobrań albumu
    # zwracany typ i opis: brak – funkcja wykonuje akcje bez zwracania wartości.
    # autor: <numer zdającego>
    # **********************************************
    def __init__(self, artist_name, album_name, songs_number, release_year, download_number):
        self.arist_name = artist_name
        self.album_name = album_name
        self.songs_number = songs_number
        self.release_year = release_year
        self.download_number = download_number
    def increase_download_number(self):
        self.download_number += 1

class Ui(QtWidgets.QMainWindow):
    # **********************************************
    # nazwa funkcji: __init__
    # opis funkcji: Konstruktor tworzenia okienka aplikacji desktopowej
    # parametry: brak
    # zwracany typ i opis: brak – funkcja wykonuje akcje bez zwracania wartości.
    # autor: <numer zdającego>
    # **********************************************
    def __init__(self):
        self.id_albumu=0
        super(Ui, self).__init__()
        uic.loadUi("untitled.ui", self)
        self.albumy = []
        with open("Data.txt") as file:
            lines = iter(file.readlines())
            while True:
                try:
                    artist_name = next(lines).strip()
                    album_name = next(lines).strip()
                    songs_number = int(next(lines).strip())
                    release_year = int(next(lines).strip())
                    download_number = int(next(lines).strip())
                    self.albumy.append(MusicAlbum(artist_name, album_name, songs_number, release_year, download_number))
                    try:
                        next(lines)
                    except StopIteration:
                        break
                except StopIteration:
                    break

        self.setWindowTitle("Moje dźwięki, Wykonał: 000000000000000")
        # Przyciski nastepny-poprzedni
        self.button_Previous = self.findChild(QtWidgets.QPushButton, "pushButton_Previous")
        self.button_Previous.clicked.connect(self.previous)
        self.button_Next = self.findChild(QtWidgets.QPushButton, "pushButton_Next")
        self.button_Next.clicked.connect(self.next)

        #Przycisk pobierania
        self.button_Download = self.findChild(QtWidgets.QPushButton, "pushButton_Download")
        self.button_Download.clicked.connect(self.download)

        self.artist_Name = self.findChild(QtWidgets.QLabel, "label_Artist_Name")
        self.artist_Name.setText(self.albumy[self.id_albumu].arist_name)
        self.album_Name = self.findChild(QtWidgets.QLabel, "label_Album_Name")
        self.album_Name.setText(self.albumy[self.id_albumu].album_name)
        self.songs_number = self.findChild(QtWidgets.QLabel, "label_Songs_Number")
        self.songs_number.setText(str(self.albumy[self.id_albumu].songs_number)+" utworów")
        self.release_year = self.findChild(QtWidgets.QLabel, "label_Release_Year")
        self.release_year.setText(str(self.albumy[self.id_albumu].release_year))
        self.download_number = self.findChild(QtWidgets.QLabel, "label_Download_Number")
        self.download_number.setText(str(self.albumy[self.id_albumu].download_number))



    def previous(self):
        self.id_albumu = self.id_albumu - 1
        if self.id_albumu < 0:
            self.id_albumu= len(self.albumy)-1
        self.artist_Name.setText(self.albumy[self.id_albumu].arist_name)
        self.album_Name.setText(self.albumy[self.id_albumu].album_name)
        self.songs_number.setText(str(self.albumy[self.id_albumu].songs_number)+" utworów")
        self.release_year.setText(str(self.albumy[self.id_albumu].release_year))
        self.download_number.setText(str(self.albumy[self.id_albumu].download_number))

    def next(self):
        self.id_albumu = self.id_albumu + 1
        if self.id_albumu > len(self.albumy)-1:
            self.id_albumu = 0
        self.artist_Name.setText(self.albumy[self.id_albumu].arist_name)
        self.album_Name.setText(self.albumy[self.id_albumu].album_name)
        self.songs_number.setText(str(self.albumy[self.id_albumu].songs_number)+" utworów")
        self.release_year.setText(str(self.albumy[self.id_albumu].release_year))
        self.download_number.setText(str(self.albumy[self.id_albumu].download_number))

    def download(self):
        self.albumy[self.id_albumu].increase_download_number()
        self.download_number.setText(str(self.albumy[self.id_albumu].download_number))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())