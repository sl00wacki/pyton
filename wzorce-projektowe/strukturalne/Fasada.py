# Klasy frameworku, które są zewnętrzne i nie mogą być zmieniane

class VideoFile:
    def __init__(self, filename: str):
        self.filename = filename

    def __str__(self):
        return f"VideoFile({self.filename})"


class OggCompressionCodec:
    def __str__(self):
        return "OggCompressionCodec"


class MPEG4CompressionCodec:
    def __str__(self):
        return "MPEG4CompressionCodec"


class CodecFactory:
    def extract(self, file: VideoFile):
        # Zwróć odpowiedni kodek w zależności od formatu pliku
        if file.filename.endswith(".ogg"):
            return OggCompressionCodec()
        else:
            return MPEG4CompressionCodec()


class BitrateReader:
    @staticmethod
    def read(filename: str, codec):
        # Zaczynaj czytanie pliku przy użyciu odpowiedniego kodeka
        print(f"Reading {filename} with {codec}")
        return f"Buffer of {filename} with {codec}"

    @staticmethod
    def convert(buffer, codec):
        # Zrób konwersję danych do nowego kodeka
        print(f"Converting buffer to {codec}")
        return f"Converted buffer with {codec}"


class AudioMixer:
    def fix(self, result):
        # Popraw audio
        print("Mixing audio")
        return f"Audio fixed for {result}"


# Klasa fasada, która upraszcza interfejs konwersji wideo

class VideoConverter:
    def convert(self, filename: str, format: str):
        file = VideoFile(filename)
        codec_factory = CodecFactory()
        source_codec = codec_factory.extract(file)

        # Wybór formatu docelowego
        if format == "mp4":
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        # Przeczytanie, konwersja, miksowanie audio
        buffer = BitrateReader.read(filename, source_codec)
        result = BitrateReader.convert(buffer, destination_codec)
        result = AudioMixer().fix(result)

        # Zwrócenie wyniku jako obiekt typu File
        return File(result)


# Klasa, która reprezentuje wynik konwersji wideo
class File:
    def __init__(self, result: str):
        self.result = result

    def save(self):
        print(f"Saving the file: {self.result}")


# Klasa aplikacji, która korzysta z klasy VideoConverter
class Application:
    def main(self):
        converter = VideoConverter()
        mp4 = converter.convert("funny-cats-video.ogg", "mp4")
        mp4.save()


# Przykład użycia
if __name__ == "__main__":
    app = Application()
    app.main()
