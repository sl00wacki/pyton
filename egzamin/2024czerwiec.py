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

    # **********************************************
    # nazwa funkcji: toString
    # opis funkcji: Funkcja zwraca pola obiektu klasy MusicAlbum
    # parametry: brak
    # zwracany typ i opis: brak – funkcja wykonuje akcje bez zwracania wartości.
    # autor: <numer zdającego>
    # **********************************************
    def toString(self):
        print(f"{self.arist_name}\n{self.album_name}\n{self.songs_number}\n{self.release_year}\n{self.download_number}\n")

if __name__ == '__main__':
    albumy = []
    with open("dataforalbum/Data.txt") as file:
            lines = iter(file.readlines())
            while True:
                try:
                    artist_name = next(lines).strip()
                    album_name = next(lines).strip()
                    songs_number = int(next(lines).strip())
                    release_year = int(next(lines).strip())
                    download_number = int(next(lines).strip())
                    albumy.append(MusicAlbum(artist_name, album_name, songs_number, release_year, download_number))
                    try:
                        next(lines)
                    except StopIteration:
                        break
                except StopIteration:
                    break
    for album in albumy:
        album.toString()