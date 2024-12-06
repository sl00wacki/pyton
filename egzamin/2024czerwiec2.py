class MusicAlbum:
    def __init__(self, artist_name, album_name, rating, release_year, sales):
        self.artist_name = artist_name
        self.album_name = album_name
        self.rating = rating
        self.release_year = release_year
        self.sales = sales
    def __print__(self):
        print(f"Wykonawca: {self.artist_name}\n"
              f"Album: {self.album_name}\n"
              f"Ocena: {self.rating}\n"
              f"Data wydania: {self.release_year}\n"
              f"Liczba sprzedanych płyt: {self.sales}\n")

if __name__ == "__main__":
    albums = []
    with open('dataforalbum/Data.txt', 'r', encoding='utf8') as file:
        lines = file.readlines()
        with open('dataforalbum/Data.txt', 'r') as file:
                lines = iter(file.readlines())
                while True:
                    try:
                        artist = next(lines).strip()
                        album = next(lines).strip()
                        songs_number = int(next(lines).strip())
                        year = int(next(lines).strip())
                        download_number = int(next(lines).strip())
                        albums.append(MusicAlbum(artist, album, songs_number, year, download_number))
                        try:
                            next(lines)
                        except StopIteration:
                            break
                    except StopIteration:
                        break

    for album in albums:
        album.__print__()