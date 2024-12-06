import re

# Funkcja 1: Odczyt pliku
def odczytaj_plik(sciezka):
    with open(sciezka, 'r', encoding='utf-8') as plik:
        return plik.readlines()

# Funkcja 2: Znajdź wyraz "funkcja"
def znajdz_wyraz(zawartosc, wyraz):
    tekst = "".join(zawartosc)
    return len(re.findall(rf'\b{wyraz}\b', tekst, flags=re.IGNORECASE))

# Funkcja 3: Znajdź linie z wyrazem "funkcja"
def linie_z_wyrazem(zawartosc, wyraz):
    return [(idx + 1, linia.strip()) for idx, linia in enumerate(zawartosc) if wyraz.lower() in linia.lower()]

# Funkcja 4: Liczba wystąpień cyfr w tekście
def liczba_cyfr(zawartosc):
    tekst = "".join(zawartosc)
    return sum(1 for znak in tekst if znak.isdigit())

# Funkcja 5: Znajdź wszystkie liczby w tekście
def znajdz_liczby(zawartosc):
    tekst = "".join(zawartosc)
    return re.findall(r'\d+', tekst)

# Funkcja 6: Ponumeruj linie
def ponumeruj_linie(zawartosc):
    return [f"{idx + 1}: {linia}" for idx, linia in enumerate(zawartosc)]

# Funkcja 7: Statystyka znaków w pliku
def statystyka_znakow(zawartosc):
    tekst = "".join(zawartosc)
    litery = sum(1 for znak in tekst if znak.isalpha())
    cyfry = sum(1 for znak in tekst if znak.isdigit())
    inne = sum(1 for znak in tekst if not znak.isalnum() and not znak.isspace())
    return {'litery': litery, 'cyfry': cyfry, 'inne': inne}

# Funkcja 8: Usuń wszystkie znaki specjalne
def usun_znaki_specjalne(zawartosc):
    return [re.sub(r'[^a-zA-Z0-9\s]', '', linia) for linia in zawartosc]

# Funkcja 9: Odwróć tekst od prawej do lewej
def odwroc_tekst(zawartosc):
    return [linia[::-1] for linia in zawartosc]

def zapisz_zmiany(sciezka_wyjscia, zawartosc):
    with open(sciezka_wyjscia, 'w', encoding='utf-8') as plik:
        plik.writelines(zawartosc)

# Główna część programu
if __name__ == "__main__":
    # Ścieżka do pliku
    sciezka = 'datas/datastring.txt'
    nowy_plik = 'datas/modifieddatastring.txt'

    # Odczyt zawartości pliku
    zawartosc = odczytaj_plik(sciezka)

    # 1. Znajdź wyraz "funkcja"
    wyraz = "funkcja"
    liczba_funkcji = znajdz_wyraz(zawartosc, wyraz)
    print(f"Wyraz '{wyraz}' występuje {liczba_funkcji} razy.")

    # 2. Znajdź linie z wyrazem "funkcja"
    linie = linie_z_wyrazem(zawartosc, wyraz)
    print("Linie zawierające słowo 'funkcja':")
    for nr, linia in linie:
        print(f"Linia {nr}: {linia}")

    # 3. Liczba wystąpień cyfr w tekście
    liczba_cyfr_w_tresci = liczba_cyfr(zawartosc)
    print(f"Liczba cyfr w pliku: {liczba_cyfr_w_tresci}")

    # 4. Znajdź wszystkie liczby w tekście
    liczby = znajdz_liczby(zawartosc)
    print("Liczby znalezione w pliku:")
    print(", ".join(liczby) if liczby else "Brak liczb.")

    # 5. Ponumeruj linie
    ponumerowane_linie = ponumeruj_linie(zawartosc)

    # 6. Statystyka znaków w pliku
    statystyka = statystyka_znakow(zawartosc)
    print("Statystyka znaków:")
    print(statystyka)

    bez_znakow_specjalnych = usun_znaki_specjalne(zawartosc)
    print("Usuwanie znakow specjalnych...")

    # 8. Odwróć tekst od prawej do lewej
    odwrocony_tekst = odwroc_tekst(bez_znakow_specjalnych)
    print("Odwracanie tekstu...")

    # Zapis zmodyfikowanego tekstu do pliku
    zapisz_zmiany(nowy_plik, odwrocony_tekst)
    print(f"Zmodyfikowany plik został zapisany jako '{nowy_plik}'.")
