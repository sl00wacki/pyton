import os
file_name='datastring.txt'

if os.path.exists(file_name):
    os.remove(file_name)
    print("Plik juz istnial. Usuniety")

with open(file_name,'w', encoding='utf-8') as file:
    file.write("""# Tekst testowy
Ten plik zawiera różne linie tekstu, aby umożliwić testowanie funkcji manipulujących stringami i odczytem plików.

1. To jest pierwsza linia tekstu.
2. Tutaj mamy drugą linię z liczbą: 42.
3. Czy funkcja znajdzie ten wyraz? Funkcja.
4. Liczby w tekście: 123, 456, 789.
5. Specjalne znaki: @#$%^&*()_+-=[]{}|;':",.<>?/!

Pusta linia poniżej:

---

Ciekawostka: Python to wspaniały język programowania.""")
print("Utworzono plik ponownie")
