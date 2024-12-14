from typing import List


# Interfejs komponentu
class DataSource:
    def writeData(self, data):
        raise NotImplementedError()

    def readData(self):
        raise NotImplementedError()


# Konkretne źródło danych: FileDataSource
class FileDataSource(DataSource):
    def __init__(self, filename: str):
        self.filename = filename

    def writeData(self, data):
        # Zapisz dane do pliku (symulacja)
        print(f"Zapisano dane do pliku {self.filename}: {data}")

    def readData(self):
        # Wczytaj dane z pliku (symulacja)
        print(f"Wczytano dane z pliku {self.filename}")
        return "Dane z pliku"


# Bazowa klasa dekorator
class DataSourceDecorator(DataSource):
    def __init__(self, source: DataSource):
        self.wrappee = source

    def writeData(self, data):
        self.wrappee.writeData(data)

    def readData(self):
        return self.wrappee.readData()


# Dekorator szyfrowania
class EncryptionDecorator(DataSourceDecorator):
    def writeData(self, data):
        # Zaszyfruj dane przed zapisaniem
        encrypted_data = f"Zaszyfrowane({data})"
        print(f"Szyfrowanie danych: {encrypted_data}")
        self.wrappee.writeData(encrypted_data)

    def readData(self):
        data = self.wrappee.readData()
        # Spróbuj odszyfrować dane
        decrypted_data = f"Odszyfrowane({data})"
        print(f"Odszyfrowywanie danych: {decrypted_data}")
        return decrypted_data


# Dekorator kompresji
class CompressionDecorator(DataSourceDecorator):
    def writeData(self, data):
        # Skompresuj dane przed zapisaniem
        compressed_data = f"Skompresowane({data})"
        print(f"Kompresja danych: {compressed_data}")
        self.wrappee.writeData(compressed_data)

    def readData(self):
        data = self.wrappee.readData()
        # Spróbuj zdekompresować dane
        decompressed_data = f"Decompressed({data})"
        print(f"Decompressing data: {decompressed_data}")
        return decompressed_data


# Menedżer danych, który korzysta z opakowanego źródła danych
class SalaryManager:
    def __init__(self, source: DataSource):
        self.source = source

    def load(self):
        return self.source.readData()

    def save(self, salaryRecords):
        self.source.writeData(salaryRecords)


# Aplikacja, która konfiguruje źródło danych i stosuje dekoratory
class ApplicationConfigurator:
    def configurationExample(self, enabledEncryption: bool, enabledCompression: bool):
        source = FileDataSource("salary.dat")

        # Dynamiczne dodawanie dekoratorów w zależności od ustawień
        if enabledEncryption:
            source = EncryptionDecorator(source)
        if enabledCompression:
            source = CompressionDecorator(source)

        # Tworzymy menedżera danych
        logger = SalaryManager(source)

        # Przykładowe operacje
        salaryRecords = "Pensja: 5000"
        print("\nZapis danych:")
        logger.save(salaryRecords)

        print("\nOdczyt danych:")
        loaded_data = logger.load()
        print(f"Odczytane dane: {loaded_data}")


# Przykład użycia
if __name__ == "__main__":
    configurator = ApplicationConfigurator()

    # Przykład 1: Włączone szyfrowanie, ale brak kompresji
    print("\nPrzykład 1 - Włączone szyfrowanie:")
    configurator.configurationExample(enabledEncryption=True, enabledCompression=False)

    # Przykład 2: Włączone kompresja i szyfrowanie
    print("\nPrzykład 2 - Włączone szyfrowanie i kompresja:")
    configurator.configurationExample(enabledEncryption=True, enabledCompression=True)
